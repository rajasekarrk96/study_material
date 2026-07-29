"""
fix_pfs_path_courses.py
========================
Fixes PathCourse table for python-full-stack path by ensuring PathCourse entries
point to the published course IDs.
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

def fix_path():
    with app.app_context():
        path = LearningPath.query.filter_by(slug="python-full-stack").first()
        if not path:
            print("ERROR: python-full-stack path not found.")
            return

        # Delete old PathCourse entries for this path
        PathCourse.query.filter_by(path_id=path.id).delete()
        db.session.commit()

        # Link all 18 published courses
        linked = 0
        for idx, slug in enumerate(PFS_SLUGS, start=1):
            course = Course.query.filter_by(slug=slug, is_deleted=False).first()
            if course:
                course.status = "published"
                pc = PathCourse(
                    path_id=path.id,
                    course_id=course.id,
                    sort_order=idx,
                    is_required=True
                )
                db.session.add(pc)
                linked += 1
                print(f"  [{idx:2d}] Linked {course.title:35s} (ID {course.id}) -> published")

        db.session.commit()
        print(f"\nSUCCESS: Linked {linked} courses to python-full-stack path!")

        from scripts.generate_roadmap_docs import build_docs
        build_docs()
        print("SUCCESS: Rebuilt all 8 roadmap documentation files!")

if __name__ == "__main__":
    fix_path()
