"""
fix_all_published_status.py
===========================
Ensures all 18 courses in Python Full Stack have status='published' in Course table,
and updates all roadmap docs.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course
from app.domains.learning_path.models import LearningPath, PathCourse

app = create_app()

PFS_SLUGS = [
    "core-python", "advanced-python", "python-dsa", "git-fundamentals",
    "html5", "css3", "bootstrap", "javascript", "jquery", "react",
    "mysql", "mongodb", "flask", "rest-api", "auth-jwt", "fastapi",
    "linux", "docker"
]

def fix_all():
    with app.app_context():
        path = LearningPath.query.filter_by(slug="python-full-stack").first()
        pcs = PathCourse.query.filter_by(path_id=path.id).all()
        
        for pc in pcs:
            c = db.session.get(Course, pc.course_id)
            c.status = "published"
            for m in c.modules.all():
                for l in m.lessons.filter_by(is_deleted=False).all():
                    l.status = "published"
        
        db.session.commit()
        print("SUCCESS: Updated status='published' for all Python Full Stack courses & lessons in DB!")

        from scripts.generate_roadmap_docs import build_docs
        build_docs()
        print("SUCCESS: Re-built all 8 roadmap documentation files!")

if __name__ == "__main__":
    fix_all()
