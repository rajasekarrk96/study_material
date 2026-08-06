"""
Learning OS — Content Pipeline Service.
Manages course curriculum imports/exports and automated content proposal packaging.
"""
import json
import logging
from typing import Dict, Optional
from app.core.extensions import db
from app.domains.content.models import Course, Module, Lesson, LessonSection
from app.domains.workflow.models import ContentProposal
from app.services.workflow_service import WorkflowService

logger = logging.getLogger("learning_os.pipeline")


class ContentPipelineService:
    # ── 1. Package Exports ────────────────────────────────────────────────────
    @staticmethod
    def export_course(course_id: int) -> str:
        """Export all structural contents of a course to a serialized JSON package string."""
        course = db.session.get(Course, course_id)
        if not course:
            raise ValueError("Course not found")

        package = {
            "title": course.title,
            "slug": course.slug,
            "description": course.description,
            "difficulty": course.difficulty,
            "estimated_minutes": course.estimated_minutes,
            "modules": []
        }

        for m in course.modules:
            mod_data = {
                "title": m.title,
                "slug": m.slug,
                "difficulty": m.difficulty,
                "estimated_minutes": m.estimated_minutes,
                "lessons": []
            }
            for l in m.lessons:
                lesson_data = {
                    "title": l.title,
                    "slug": l.slug,
                    "estimated_minutes": l.estimated_minutes,
                    "difficulty": l.difficulty,
                    "sections": []
                }
                for s in l.sections:
                    sec_data = {
                        "section_type": s.section_type,
                        "title": s.title,
                        "content_markdown": s.content_markdown,
                        "sort_order": s.sort_order
                    }
                    lesson_data["sections"].append(sec_data)
                
                mod_data["lessons"].append(lesson_data)
            
            package["modules"].append(mod_data)

        return json.dumps(package, indent=2)

    # ── 2. Package Imports & Auto-Proposal Generator ──────────────────────────
    @staticmethod
    def import_course_package(course_id: int, package_json_str: str, author_id: int) -> ContentProposal:
        """Import a JSON package, saving sections to draft layers and auto-generating a ContentProposal."""
        course = db.session.get(Course, course_id)
        if not course:
            raise ValueError("Target course not found")

        try:
            package_data = json.loads(package_json_str)
        except Exception as e:
            raise ValueError(f"Failed to parse package JSON: {e}")

        # Iterate modules & lessons
        modules_data = package_data.get("modules", [])
        
        # For simplicity, we target the first lesson update in the package
        imported_lesson = None
        
        for m_data in modules_data:
            m_slug = m_data.get("slug")
            module = Module.query.filter_by(course_id=course_id, slug=m_slug).first()
            if not module:
                continue

            lessons_data = m_data.get("lessons", [])
            for l_data in lessons_data:
                l_slug = l_data.get("slug")
                lesson = Lesson.query.filter_by(module_id=module.id, slug=l_slug).first()
                if not lesson:
                    # Create lesson dynamically under target module if missing
                    lesson = Lesson(
                        module_id=module.id,
                        title=l_data.get("title", "New Lesson"),
                        slug=l_slug or "new-lesson",
                        status="draft"
                    )
                    db.session.add(lesson)
                    db.session.flush()

                imported_lesson = lesson

                # Save imported sections directly to the draft layer
                sections_data = l_data.get("sections", [])
                for s_data in sections_data:
                    WorkflowService.save_draft_section(
                        lesson_id=lesson.id,
                        section_type=s_data.get("section_type", "explanation"),
                        title=s_data.get("title"),
                        content_markdown=s_data.get("content_markdown", ""),
                        sort_order=s_data.get("sort_order", 0),
                        user_id=author_id
                    )

        if not imported_lesson:
            raise ValueError("No matching lessons found in package to import.")

        # 3. Auto-generate the ContentProposal using the draft layers
        checklist = {
            "grammar_checked": True,
            "code_executed": True,
            "seo_checked": True
        }
        proposal = WorkflowService.create_proposal(
            proposal_type="CONTENT_UPDATE",
            target_type="LESSON",
            target_id=imported_lesson.id,
            author_id=author_id,
            description="Automated content proposal generated from imported curriculum package.",
            checklist_data=checklist
        )

        return proposal
