"""Audit all existing courses, modules, and lessons for curriculum comparison."""
import sys, json
sys.path.insert(0, r'd:\My Drive\all files\PROJECT FILES\notes')
from app import create_app
from app.domains.content.models import Course, Module, Lesson

app = create_app()
with app.app_context():
    relevant = [
        'c-programming','core-python','git','git','mysql','flask',
        'html5','css3','bootstrap','javascript','fastapi','embedded-c',
        'arduino','esp32','raspberry-pi','sensors-actuators','advanced-components',
        'mqtt','iot-cloud','basic-ml-iot','computer-vision-iot','basic-matlab',
        'simulation','core-java','java','selenium'
    ]
    for slug in relevant:
        c = Course.query.filter_by(slug=slug, is_deleted=False).first()
        if not c:
            print(f"\nCOURSE NOT FOUND: {slug}")
            continue
        mods = c.modules.all()
        print(f"\n{'='*60}")
        print(f"COURSE: {c.title} (slug={c.slug}, id={c.id})")
        print(f"  Modules: {len(mods)}  |  Estimated: {c.estimated_hours}h")
        for m in mods:
            lessons = m.lessons.filter_by(is_deleted=False).all()
            print(f"  MOD [{m.sort_order:2d}]: {m.title}  ({len(lessons)} lessons)")
            for l in lessons[:5]:
                print(f"          L: {l.title}")
            if len(lessons) > 5:
                print(f"          ... and {len(lessons)-5} more lessons")
