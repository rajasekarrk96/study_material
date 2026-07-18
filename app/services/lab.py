"""
Learning OS — Interactive Lab Service Layer
"""
import re
from datetime import datetime
from app.core.extensions import db
from app.domains.content.models import Lab, LabStep, LabSubmission
from app.services.lab_validation import LabValidationEngine
from app.services.learning import EventService

class LabService:
    @staticmethod
    def get_lab(lab_id: int) -> Lab:
        return db.session.get(Lab, lab_id)

    @staticmethod
    def get_submission(user_id: int, lab_id: int) -> LabSubmission:
        return LabSubmission.query.filter_by(user_id=user_id, lab_id=lab_id).first()

    @staticmethod
    def submit_step_progress(user_id: int, lab_id: int, step_number: int, is_completed: bool) -> LabSubmission:
        """Mark a specific step of the lab as completed in the draft submission."""
        sub = LabService.get_submission(user_id, lab_id)
        if not sub:
            sub = LabSubmission(
                user_id=user_id,
                lab_id=lab_id,
                submission_data={"completed_steps": []},
                status="submitted"
            )
            db.session.add(sub)
        
        data = dict(sub.submission_data or {})
        completed_steps = list(data.get("completed_steps", []))
        
        if is_completed:
            if step_number not in completed_steps:
                completed_steps.append(step_number)
        else:
            if step_number in completed_steps:
                completed_steps.remove(step_number)
                
        data["completed_steps"] = completed_steps
        sub.submission_data = data
        db.session.commit()
        return sub

    @staticmethod
    def verify_and_grade_lab(user_id: int, lab_id: int, repo_path: str = None) -> LabSubmission:
        """
        Verify the status of the lab. For guided labs, verify all steps are checked.
        For Git repositories, execute validators on the repository path.
        """
        lab = LabService.get_lab(lab_id)
        if not lab:
            return None

        sub = LabService.get_submission(user_id, lab_id)
        if not sub:
            sub = LabSubmission(
                user_id=user_id,
                lab_id=lab_id,
                submission_data={"completed_steps": []},
                status="submitted"
            )
            db.session.add(sub)

        # Retrieve steps
        steps = LabStep.query.filter_by(lab_id=lab_id).order_by(LabStep.step_number).all()
        
        # Guided check
        data = dict(sub.submission_data or {})
        completed_steps = list(data.get("completed_steps", []))
        
        all_passed = True
        feedback_parts = []
        
        for step in steps:
            rule = None
            expected = None
            
            # Simple metadata parser from step instruction
            # e.g. "<!-- rule:git_init -->" or "<!-- rule:git_commit expected:initial -->"
            match = re.search(r"<!--\s*rule:(\w+)(?:\s+expected:([^\s>-]+))?\s*-->", step.instruction)
            if match:
                rule = match.group(1)
                expected = match.group(2)
                
            if rule:
                if not repo_path:
                    all_passed = False
                    feedback_parts.append(f"Step {step.step_number} ({step.title or 'Git Step'}): Missing repository path for verification.")
                    continue
                
                success, msg = LabValidationEngine.validate_local_git_repo(repo_path, rule, expected)
                feedback_parts.append(f"Step {step.step_number} ({step.title or 'Git Step'}): {msg}")
                if not success:
                    all_passed = False
                else:
                    # Update completed steps draft
                    if step.step_number not in completed_steps:
                        completed_steps.append(step.step_number)
            else:
                # Guided check: must be marked complete manually in UI
                if step.step_number not in completed_steps:
                    all_passed = False
                    feedback_parts.append(f"Step {step.step_number} ({step.title or 'Step'}): Must be marked completed manually.")
                else:
                    feedback_parts.append(f"Step {step.step_number} ({step.title or 'Step'}): Completed manually.")

        # Update completed steps list in JSON
        data["completed_steps"] = completed_steps
        if repo_path:
            data["repo_path"] = repo_path
        sub.submission_data = data

        # Final outcome
        sub.feedback = "\n".join(feedback_parts)
        
        if all_passed:
            sub.status = "passed"
            db.session.commit()
            
            # Publish event
            EventService.publish("lab_completed", user_id=user_id, lab_id=lab_id)
        else:
            sub.status = "failed"
            db.session.commit()

        return sub
