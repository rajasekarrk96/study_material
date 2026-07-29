"""
setup_java_fullstack_v3.py
==========================
1. Keep both Java courses but clarify their distinction
2. Make Java (id=60001) optional in Java Full Stack path
3. Create Spring Boot and Hibernate stub courses (no lessons yet)
4. Add Spring Boot, Hibernate, Git to Java Full Stack path
"""
import sys
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')
from datetime import datetime
from app import create_app
from app.core.extensions import db
from app.domains.content.models import Category, Subject, Course
from app.domains.learning_path.models import LearningPath, PathCourse

app = create_app()

with app.app_context():

    # ── 1. Make Java (60001) optional in Java Full Stack ──────────────────
    path = LearningPath.query.filter_by(slug='java-full-stack').first()
    java_course = Course.query.filter_by(slug='java', is_deleted=False).first()
    if java_course and path:
        pc = PathCourse.query.filter_by(path_id=path.id, course_id=java_course.id).first()
        if pc:
            pc.is_required = False
            print(f'[OK] Java (60001) -> optional in Java Full Stack')

    # ── 2. Get/create Backend Development category ────────────────────────
    backend_cat = Category.query.filter_by(slug='backend-development').first()
    prog_cat    = Category.query.filter_by(slug='programming-languages').first()

    # ── 3. Get or create Java subject under Programming Languages ─────────
    java_subj = Subject.query.filter_by(slug='java', category_id=prog_cat.id).first()
    if not java_subj:
        java_subj = Subject.query.filter_by(slug='java').first()

    # ── 4. Create Spring Boot stub course ─────────────────────────────────
    spring = Course.query.filter_by(slug='spring-boot', is_deleted=False).first()
    if not spring:
        # Find or create a subject for Spring Boot under Backend Development
        sb_subj = Subject.query.filter_by(slug='spring-boot').first()
        if not sb_subj:
            sb_subj = Subject(
                name='Spring Boot',
                slug='spring-boot',
                category_id=backend_cat.id,
                description='Java Spring Boot framework for building enterprise web apps and REST APIs.'
            )
            db.session.add(sb_subj)
            db.session.flush()

        spring = Course(
            subject_id=sb_subj.id,
            title='Spring Boot',
            slug='spring-boot',
            description='Build enterprise-grade Java web applications and REST APIs using Spring Boot, Spring MVC, Spring Data JPA, and Spring Security.',
            difficulty_level='intermediate',
            status='published',
            is_deleted=False,
            estimated_hours=30,
            is_featured=False,
        )
        db.session.add(spring)
        db.session.flush()
        print(f'[CREATE] Spring Boot course (id={spring.id})')
    else:
        print(f'[EXISTS] Spring Boot course (id={spring.id})')

    # ── 5. Create Hibernate stub course ───────────────────────────────────
    hibernate = Course.query.filter_by(slug='hibernate', is_deleted=False).first()
    if not hibernate:
        hib_subj = Subject.query.filter_by(slug='hibernate').first()
        if not hib_subj:
            hib_subj = Subject(
                name='Hibernate',
                slug='hibernate',
                category_id=backend_cat.id,
                description='Java ORM framework for database persistence using Hibernate and JPA.'
            )
            db.session.add(hib_subj)
            db.session.flush()

        hibernate = Course(
            subject_id=hib_subj.id,
            title='Hibernate & JPA',
            slug='hibernate',
            description='Master Java persistence with Hibernate ORM and JPA — entities, relationships, HQL, caching, and transactions.',
            difficulty_level='intermediate',
            status='published',
            is_deleted=False,
            estimated_hours=20,
            is_featured=False,
        )
        db.session.add(hibernate)
        db.session.flush()
        print(f'[CREATE] Hibernate & JPA course (id={hibernate.id})')
    else:
        print(f'[EXISTS] Hibernate course (id={hibernate.id})')

    # ── 6. Add Spring Boot, Hibernate, Git to Java Full Stack path ────────
    git = Course.query.filter_by(slug='git', is_deleted=False).first()

    new_entries = [
        (spring.id,   'Frameworks',      8,  True),
        (hibernate.id,'Frameworks',      9,  True),
    ]
    if git:
        new_entries.append((git.id, 'Version Control', 10, True))

    for (course_id, section, sort, required) in new_entries:
        existing = PathCourse.query.filter_by(
            path_id=path.id, course_id=course_id
        ).first()
        if not existing:
            pc = PathCourse(
                path_id=path.id,
                course_id=course_id,
                sort_order=sort,
                is_required=required,
                section_label=section,
            )
            db.session.add(pc)
            c = Course.query.get(course_id)
            print(f'  [ADD] {section}: {c.title}')
        else:
            print(f'  [EXISTS] already in path: course_id={course_id}')

    # Recalculate estimated hours for the path
    db.session.flush()
    path.estimated_hours = sum(
        (pc.course.estimated_hours or 0) for pc in path.courses if pc.course
    )

    db.session.commit()
    print(f'\n[OK] Committed. Java Full Stack estimated_hours={path.estimated_hours}h')

    print('\nFinal Java Full Stack curriculum:')
    for pc in path.courses:
        status = 'required' if pc.is_required else 'optional'
        print(f'  [{pc.section_label}] {pc.course.title} ({status})')
