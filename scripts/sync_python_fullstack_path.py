"""
sync_python_fullstack_path.py
==============================
Links all 18 Python Full Stack courses to the python-full-stack Learning Path in PathCourse table,
ensuring 100% path completion status across the database and roadmap docs.
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')

from app import create_app
from app.core.extensions import db
from app.domains.content.models import Course
from app.domains.learning_path.models import LearningPath, PathCourse

app = create_app()

PFS_SLUGS = [
    "core-python", "advanced-python", "python-dsa", "git",
    "html5", "css3", "bootstrap", "javascript", "jquery", "react",
    "mysql", "mongodb", "flask", "rest-api", "auth-jwt", "fastapi",
    "linux", "docker"
]

def sync_pfs():
    with app.app_context():
        path = LearningPath.query.filter_by(slug="python-full-stack").first()
        if not path:
            print("ERROR: python-full-stack path not found.")
            return

        existing_pcs = {pc.course_id: pc for pc in PathCourse.query.filter_by(path_id=path.id).all()}
        
        linked_count = 0
        for idx, slug in enumerate(PFS_SLUGS, start=1):
            course = Course.query.filter_by(slug=slug, is_deleted=False).first()
            if not course:
                print(f"[WARNING] Course slug {slug} not found.")
                continue

            course.status = "published"
            
            pc = existing_pcs.get(course.id)
            if not pc:
                pc = PathCourse(
                    path_id=path.id,
                    course_id=course.id,
                    sort_order=idx,
                    is_required=True
                )
                db.session.add(pc)
                linked_count += 1
            else:
                pc.sort_order = idx

        db.session.commit()
        print(f"SUCCESS: Synchronized {len(PFS_SLUGS)} courses for python-full-stack path (linked {linked_count} new entries).")

        # Re-run generate_roadmap_docs
        from scripts.generate_roadmap_docs import build_docs
        build_docs()
        print("SUCCESS: Updated all roadmap documentation files!")

if __name__ == "__main__":
    sync_pfs()
