"""
Learning OS — Editorial Workflow Domain Models
DraftLessonSections, ContentProposals, ContentProposalSections, AIProposalReviews, ContentVersions, CurriculumReleases, Approvals, ReviewComments, ActivityLogs, NotificationQueues.
"""
from datetime import datetime
from app.core.extensions import db
from app.core.base_model import TimestampMixin


class DraftLessonSection(db.Model, TimestampMixin):
    __tablename__ = "draft_lesson_sections"

    id = db.Column(db.Integer, primary_key=True)
    lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=False)
    section_type = db.Column(db.String(50), nullable=False)
    title = db.Column(db.String(255), nullable=True)
    content_markdown = db.Column(db.Text, nullable=True)
    sort_order = db.Column(db.Integer, default=0)
    last_saved_by_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)

    def __repr__(self):
        return f"<DraftLessonSection lesson={self.lesson_id} type={self.section_type}>"


class ContentProposal(db.Model, TimestampMixin):
    __tablename__ = "content_proposals"

    id = db.Column(db.Integer, primary_key=True)
    proposal_type = db.Column(db.String(50), nullable=False)  # CONTENT_UPDATE, NEW_LESSON, etc.
    target_type = db.Column(db.String(50), nullable=False)    # COURSE, MODULE, LESSON, TOPIC, SECTION
    target_id = db.Column(db.Integer, nullable=True)
    draft_lesson_id = db.Column(db.Integer, db.ForeignKey("lessons.id"), nullable=True)
    author_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    description = db.Column(db.Text, nullable=True)
    status = db.Column(db.String(50), default="Draft", nullable=False)  # Draft, Submitted, AI_Review, Pending_Review, etc.

    # Proposal Checklist
    grammar_checked = db.Column(db.Boolean, default=False, nullable=False)
    code_executed = db.Column(db.Boolean, default=False, nullable=False)
    images_added = db.Column(db.Boolean, default=False, nullable=False)
    quiz_updated = db.Column(db.Boolean, default=False, nullable=False)
    references_added = db.Column(db.Boolean, default=False, nullable=False)
    seo_checked = db.Column(db.Boolean, default=False, nullable=False)
    accessibility_checked = db.Column(db.Boolean, default=False, nullable=False)

    proposal_sections = db.relationship("ContentProposalSection", back_populates="proposal", cascade="all, delete-orphan")
    ai_reviews = db.relationship("AIProposalReview", back_populates="proposal", cascade="all, delete-orphan")
    approvals = db.relationship("Approval", back_populates="proposal", cascade="all, delete-orphan")
    comments = db.relationship("ReviewComment", back_populates="proposal", cascade="all, delete-orphan")

    def __repr__(self):
        return f"<ContentProposal id={self.id} type={self.proposal_type} status={self.status}>"


class ContentProposalSection(db.Model):
    __tablename__ = "content_proposal_sections"

    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("content_proposals.id"), nullable=False)
    lesson_section_id = db.Column(db.Integer, db.ForeignKey("lesson_sections.id"), nullable=True)
    title = db.Column(db.String(255), nullable=True)
    new_content = db.Column(db.Text, nullable=True)

    proposal = db.relationship("ContentProposal", back_populates="proposal_sections")
    lesson_section = db.relationship("LessonSection")

    def __repr__(self):
        return f"<ContentProposalSection proposal={self.proposal_id} section={self.lesson_section_id}>"


class AIProposalReview(db.Model, TimestampMixin):
    __tablename__ = "ai_proposal_reviews"

    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("content_proposals.id"), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # Passed, Failed, Flagged
    feedback_json = db.Column(db.Text, nullable=True)  # Stores review breakdown
    ai_generated = db.Column(db.Boolean, default=False, nullable=False)
    generated_by = db.Column(db.String(100), nullable=True)  # Gemini, OpenAI, Claude, Manual
    model_version = db.Column(db.String(100), nullable=True)

    proposal = db.relationship("ContentProposal", back_populates="ai_reviews")

    def __repr__(self):
        return f"<AIProposalReview proposal={self.proposal_id} status={self.status}>"


class ContentVersion(db.Model):
    __tablename__ = "content_versions"

    id = db.Column(db.Integer, primary_key=True)
    target_type = db.Column(db.String(50), nullable=False)  # COURSE, MODULE, LESSON, TOPIC, QUIZ, LAB, SYLLABUS
    target_id = db.Column(db.Integer, nullable=False)
    version_number = db.Column(db.Integer, nullable=False)
    merged_by_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=True)
    snapshot_json = db.Column(db.Text, nullable=False)  # JSON representation of target structure
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<ContentVersion {self.target_type}:{self.target_id} v{self.version_number}>"


class CurriculumRelease(db.Model):
    __tablename__ = "curriculum_releases"

    id = db.Column(db.Integer, primary_key=True)
    version_name = db.Column(db.String(255), nullable=False)
    semesterly_tag = db.Column(db.String(100), nullable=False)
    snapshot_json = db.Column(db.Text, nullable=False)
    is_active_for_new_enrollments = db.Column(db.Boolean, default=True, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<CurriculumRelease {self.version_name}>"


class Approval(db.Model, TimestampMixin):
    __tablename__ = "approvals"

    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("content_proposals.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    status = db.Column(db.String(50), nullable=False)  # approved, rejected, changes_requested
    comments = db.Column(db.Text, nullable=True)

    proposal = db.relationship("ContentProposal", back_populates="approvals")

    def __repr__(self):
        return f"<Approval proposal={self.proposal_id} user={self.user_id} status={self.status}>"


class ReviewComment(db.Model, TimestampMixin):
    __tablename__ = "review_comments"

    id = db.Column(db.Integer, primary_key=True)
    proposal_id = db.Column(db.Integer, db.ForeignKey("content_proposals.id"), nullable=False)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    comment = db.Column(db.Text, nullable=False)

    proposal = db.relationship("ContentProposal", back_populates="comments")

    def __repr__(self):
        return f"<ReviewComment proposal={self.proposal_id} user={self.user_id}>"


class ActivityLog(db.Model):
    __tablename__ = "activity_logs"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    action = db.Column(db.String(50), nullable=False)  # Created, Updated, Approved, Rejected, Merged, Published
    target_type = db.Column(db.String(50), nullable=False)
    target_id = db.Column(db.Integer, nullable=True)
    details = db.Column(db.Text, nullable=True)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<ActivityLog user={self.user_id} action={self.action}>"


class NotificationQueue(db.Model):
    __tablename__ = "notification_queue"

    id = db.Column(db.Integer, primary_key=True)
    user_id = db.Column(db.Integer, db.ForeignKey("users.id"), nullable=False)
    category = db.Column(db.String(50), nullable=False)  # System, Proposal, Review, Enrollment, Course, etc.
    title = db.Column(db.String(255), nullable=False)
    message = db.Column(db.Text, nullable=False)
    is_read = db.Column(db.Boolean, default=False, nullable=False)
    created_at = db.Column(db.DateTime, default=datetime.utcnow, nullable=False)

    def __repr__(self):
        return f"<NotificationQueue user={self.user_id} title={self.title}>"
