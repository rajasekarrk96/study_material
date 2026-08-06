"""
Learning OS — Curriculum Layer Service.
Manages Course Categories, Topic Coverage status history, course/lesson prerequisites, and Roadmap Graph Nodes/Edges.
"""
import logging
from typing import List, Dict, Optional
from datetime import datetime
from app.core.extensions import db
from app.domains.content.models import (
    CourseCategory, Course, Lesson, LessonSection, TopicCoverage, TopicCoverageHistory,
    CoursePrerequisite, LessonPrerequisite, RoadmapNode, RoadmapEdge
)

logger = logging.getLogger("learning_os.curriculum")


class CurriculumService:
    # ── 1. Course Categories ──────────────────────────────────────────────────
    @staticmethod
    def get_or_create_course_category(name: str, slug: str, status: str = "ACTIVE") -> CourseCategory:
        """Find or create a course category."""
        cat = CourseCategory.query.filter_by(slug=slug).first()
        if not cat:
            cat = CourseCategory(name=name, slug=slug, status=status)
            db.session.add(cat)
            db.session.commit()
        return cat

    @staticmethod
    def list_course_categories() -> List[CourseCategory]:
        """List all active course categories."""
        return CourseCategory.query.filter_by(status="ACTIVE").all()

    # ── 2. Topic Coverage & Audits ────────────────────────────────────────────
    @staticmethod
    def get_topic_coverage(lesson_section_id: int) -> Optional[TopicCoverage]:
        """Retrieve topic coverage status details for a lesson section."""
        return TopicCoverage.query.filter_by(lesson_section_id=lesson_section_id).first()

    @staticmethod
    def update_topic_coverage(
        lesson_section_id: int,
        coverage_status: str,  # COVERED, OPTIONAL, SELF_LEARNING
        display_label: str,
        updated_by_id: Optional[int] = None
    ) -> TopicCoverage:
        """Update coverage status of a section, tracking history audit logs."""
        coverage = TopicCoverage.query.filter_by(lesson_section_id=lesson_section_id).first()
        old_status = None

        if not coverage:
            coverage = TopicCoverage(
                lesson_section_id=lesson_section_id,
                coverage_status=coverage_status,
                display_label=display_label,
                updated_by_id=updated_by_id
            )
            db.session.add(coverage)
            db.session.flush()
        else:
            old_status = coverage.coverage_status
            coverage.coverage_status = coverage_status
            coverage.display_label = display_label
            coverage.updated_by_id = updated_by_id

        # Write to audit history
        history = TopicCoverageHistory(
            topic_coverage_id=coverage.id,
            old_coverage_status=old_status,
            new_coverage_status=coverage_status,
            updated_by_id=updated_by_id,
            updated_at=datetime.utcnow()
        )
        db.session.add(history)
        db.session.commit()
        return coverage

    # ── 3. Prerequisites ─────────────────────────────────────────────────────
    @staticmethod
    def add_course_prerequisite(course_id: int, prerequisite_course_id: int) -> bool:
        """Link a prerequisite course dependency constraint."""
        exists = CoursePrerequisite.query.filter_by(
            course_id=course_id,
            prerequisite_course_id=prerequisite_course_id
        ).first()

        if not exists:
            prereq = CoursePrerequisite(course_id=course_id, prerequisite_course_id=prerequisite_course_id)
            db.session.add(prereq)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_course_prerequisites(course_id: int) -> List[Course]:
        """Fetch all courses required before taking this course."""
        links = CoursePrerequisite.query.filter_by(course_id=course_id).all()
        prereq_ids = [link.prerequisite_course_id for link in links]
        if not prereq_ids:
            return []
        return Course.query.filter(Course.id.in_(prereq_ids)).all()

    @staticmethod
    def add_lesson_prerequisite(lesson_id: int, prerequisite_lesson_id: int) -> bool:
        """Link a prerequisite lesson dependency constraint."""
        exists = LessonPrerequisite.query.filter_by(
            lesson_id=lesson_id,
            prerequisite_lesson_id=prerequisite_lesson_id
        ).first()

        if not exists:
            prereq = LessonPrerequisite(lesson_id=lesson_id, prerequisite_lesson_id=prerequisite_lesson_id)
            db.session.add(prereq)
            db.session.commit()
            return True
        return False

    @staticmethod
    def get_lesson_prerequisites(lesson_id: int) -> List[Lesson]:
        """Fetch all lessons required before unlocking this lesson."""
        links = LessonPrerequisite.query.filter_by(lesson_id=lesson_id).all()
        prereq_ids = [link.prerequisite_lesson_id for link in links]
        if not prereq_ids:
            return []
        return Lesson.query.filter(Lesson.id.in_(prereq_ids)).all()

    # ── 4. Roadmap Graph Nodes & Edges ───────────────────────────────────────
    @staticmethod
    def add_roadmap_node(title: str, node_type: str, course_id: Optional[int] = None) -> RoadmapNode:
        """Create a node in the curriculum roadmap graph."""
        node = RoadmapNode(title=title, node_type=node_type, course_id=course_id)
        db.session.add(node)
        db.session.commit()
        return node

    @staticmethod
    def add_roadmap_edge(source_node_id: int, target_node_id: int) -> RoadmapEdge:
        """Connect two roadmap graph nodes with a directed edge constraint."""
        edge = RoadmapEdge.query.filter_by(
            source_node_id=source_node_id,
            target_node_id=target_node_id
        ).first()

        if not edge:
            edge = RoadmapEdge(source_node_id=source_node_id, target_node_id=target_node_id)
            db.session.add(edge)
            db.session.commit()
        return edge

    @staticmethod
    def get_roadmap_graph() -> Dict[str, List]:
        """Compile nodes and directed edges of the sitemap roadmap graph for rendering."""
        nodes = RoadmapNode.query.all()
        edges = RoadmapEdge.query.all()

        return {
            "nodes": [{
                "id": n.id,
                "title": n.title,
                "node_type": n.node_type,
                "course_id": n.course_id
            } for n in nodes],
            "edges": [{
                "id": e.id,
                "source_node_id": e.source_node_id,
                "target_node_id": e.target_node_id
            } for e in edges]
        }
