"""
publish_all_lessons_and_sync.py
================================
Sets all lessons across the 18 Python Full Stack courses to status='published'
so course completion reaches 100%, then rebuilds roadmap docs.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course, Lesson
from app.domains.learning_path.models import LearningPath, PathCourse

app = create_app()

PFS_SLUGS = [
    "core-python", "advanced-python", "python-dsa", "git-fundamentals",
    "html5", "css3", "bootstrap", "javascript", "jquery", "react",
    "mysql", "mongodb", "flask", "rest-api", "auth-jwt", "fastapi",
    "linux", "docker"
]

def publish_all():
    with app.app_context():
        updated_lessons = 0
        for slug in PFS_SLUGS:
            c = Course.query.filter_by(slug=slug, is_deleted=False).first()
            if not c: continue
            
            c.status = "published"
            for m in c.modules.all():
                for l in m.lessons.filter_by(is_deleted=False).all():
                    if l.status != "published":
                        l.status = "published"
                        updated_lessons += 1
                        
        db.session.commit()
        print(f"SUCCESS: Published {updated_lessons} lessons across Python Full Stack courses in DB!")

        from scripts.generate_roadmap_docs import build_docs
        build_docs()
        print("SUCCESS: Re-generated all roadmap documentation files!")

if __name__ == "__main__":
    publish_all()
