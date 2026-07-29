import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')
from app import create_app
from app.core.extensions import db
from app.domains.learning_path.models import LearningPath, PathCourse
from app.domains.content.models import Course

app = create_app()
with app.app_context():
    path = LearningPath.query.filter_by(slug='python-full-stack').first()
    make_optional = ['jquery', 'fastapi', 'mongodb']
    for slug in make_optional:
        course = Course.query.filter_by(slug=slug, is_deleted=False).first()
        if course:
            pc = PathCourse.query.filter_by(path_id=path.id, course_id=course.id).first()
            if pc:
                pc.is_required = False
                print(f'[OK] {course.title} -> optional')
    db.session.commit()
    print('\nFinal Python Full Stack curriculum:')
    for pc in path.courses:
        status = 'required' if pc.is_required else 'optional'
        print(f'  [{pc.section_label}] {pc.course.title} ({status})')
