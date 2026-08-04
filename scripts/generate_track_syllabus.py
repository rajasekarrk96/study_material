#!/usr/bin/env python3
"""
Bytes and Boards Solutions — Track Syllabus Merger.
Reads the per-course syllabus docs already generated under docs/syllabus/
(by generate_syllabus_docs.py / generate_syllabus_from_db.py) and merges them
into one combined file per learning track (Java Full Stack, Data Science, ...).
Each course's own headings are demoted so the result nests cleanly under
Track -> Term -> Course -> Module -> Lesson.
"""
import re
from pathlib import Path

SYLLABUS_DIR = Path("docs/syllabus")

# slug -> display title, for course files referenced below
COURSE_TITLES = {}


def slug_to_title(slug: str) -> str:
    if slug in COURSE_TITLES:
        return COURSE_TITLES[slug]
    path = SYLLABUS_DIR / f"{slug}.md"
    if path.exists():
        first_line = path.read_text(encoding="utf-8").splitlines()[0]
        title = first_line.lstrip("#").strip()
        title = re.sub(r"\s*—\s*Syllabus$", "", title)
        return title
    return slug.replace("-", " ").title()


_HEADING_RE = re.compile(r"^(#+)(\s.*)$")


def render_course(slug: str) -> str:
    path = SYLLABUS_DIR / f"{slug}.md"
    if not path.exists():
        return f"### {slug_to_title(slug)}\n\n*(syllabus not yet available)*\n"
    lines = path.read_text(encoding="utf-8").splitlines()[1:]  # drop the "# X — Syllabus" line
    demoted = []
    for line in lines:
        # Shift every heading down by 2 levels (## -> ####, ### -> #####, ...)
        # so any depth in the source course file nests correctly under this
        # course's own "### <Course>" heading, not just a hardcoded "## ".
        m = _HEADING_RE.match(line)
        demoted.append("##" + line if m else line)
    body = "\n".join(demoted).strip("\n")
    return f"### {slug_to_title(slug)}\n\n{body}\n"


def render_track(title: str, structure) -> str:
    """structure is either a flat list of slugs, or a dict of {term_label: [slugs]}."""
    out = [f"# {title} — Syllabus", ""]
    if isinstance(structure, dict):
        for term_label, slugs in structure.items():
            out.append(f"## {term_label}")
            out.append("")
            for slug in slugs:
                out.append(render_course(slug))
    else:
        for slug in structure:
            out.append(render_course(slug))
    return "\n".join(out)


# (output_slug, display_title, structure)
TRACKS = [
    ("java-full-stack", "Java Full Stack", {
        "Term 1": ["html5", "css3", "bootstrap", "javascript", "jquery", "mysql", "sql-server", "java"],
        "Term 2": ["spring", "spring-boot", "spring-mvc", "spring-security", "hibernate", "servlet-jsp", "maven",
                   "rest-api", "auth-jwt", "react", "git", "git-fundamentals", "github-actions", "java-selenium",
                   "selenium", "postman", "docker", "jenkins", "kubernetes", "linux", "bash"],
    }),
    ("python-full-stack", "Python Full Stack", {
        "Term 1": ["html5", "css3", "bootstrap", "javascript", "jquery", "mysql", "sql-server", "python", "advanced-python"],
        "Term 2": ["flask", "fastapi", "rest-api", "auth-jwt", "react", "git", "git-fundamentals", "github-actions",
                   "selenium", "playwright", "postman", "docker", "kubernetes", "jenkins", "linux", "bash"],
    }),
    ("data-analyst", "Data Analyst", [
        "python", "python-data-science", "ds-math", "mysql", "sql-server", "power-bi", "python-dsa",
        "git", "git-fundamentals", "postman", "mongodb",
    ]),
    ("data-science", "Data Science", {
        "Term 1": ["python", "python-data-science", "ds-math", "mysql", "sql-server", "power-bi"],
        "Term 2": ["machine-learning", "deep-learning", "generative-ai-llms", "ai-agents", "prompt-engineering",
                   "rag-engineering", "nlp", "computer-vision", "mlops-ai-deployment", "git", "git-fundamentals",
                   "docker", "kubernetes"],
    }),
    ("iot-full-stack", "IoT Full Stack", {
        "Term 1": ["embedded-c", "python", "electrical-fundamentals", "electronics-basics", "sensors-actuators",
                   "esp32", "arduino", "raspberry-pi", "iot-hardware", "simulation", "html5", "css3", "bootstrap",
                   "javascript"],
        "Term 2": ["basic-ml-iot", "iot-cloud", "iot-projects", "mqtt", "computer-vision-iot", "advanced-components",
                   "mysql", "flask", "basic-matlab", "pcb", "stm32", "git", "git-fundamentals"],
    }),
    ("cloud-computing", "Cloud Computing", [
        "aws", "linux", "bash", "docker", "kubernetes", "jenkins", "git", "git-fundamentals", "github-actions",
    ]),
    ("devops", "DevOps", [
        "git", "git-fundamentals", "github-actions", "docker", "kubernetes", "jenkins", "linux", "bash", "maven",
    ]),
    ("git-version-control", "Git & Version Control", ["git", "git-fundamentals", "github-actions"]),
    ("linux-administration", "Linux Administration", ["linux", "bash"]),
    ("rest-api-development", "REST API Development", ["rest-api", "auth-jwt", "postman", "flask", "fastapi"]),
    ("software-testing", "Software Testing", ["manual-testing", "selenium", "java-selenium", "playwright", "postman"]),
    ("react-frontend", "React Frontend", ["html5", "css3", "bootstrap", "javascript", "jquery", "react", "git"]),
    ("ai-engineering", "AI Engineering", [
        "python", "advanced-python", "machine-learning", "deep-learning", "generative-ai-llms", "ai-agents",
        "prompt-engineering", "rag-engineering", "computer-vision", "nlp", "mlops-ai-deployment", "docker",
        "kubernetes", "git", "git-fundamentals",
    ]),
    ("mlops-engineering", "MLOps Engineering", [
        "mlops-ai-deployment", "docker", "kubernetes", "jenkins", "github-actions", "git", "git-fundamentals",
    ]),
    ("computer-vision", "Computer Vision", ["python", "machine-learning", "deep-learning", "computer-vision", "computer-vision-iot"]),
    ("nlp-generative-ai", "NLP & Generative AI", ["python", "nlp", "generative-ai-llms", "prompt-engineering", "rag-engineering", "ai-agents"]),
    ("embedded-systems", "Embedded Systems", [
        "embedded-c", "electrical-fundamentals", "electronics-basics", "sensors-actuators", "advanced-components",
        "pcb", "stm32", "esp32", "arduino", "raspberry-pi",
    ]),
    ("electronics-pcb-design", "Electronics & PCB Design", [
        "electrical-fundamentals", "electronics-basics", "pcb", "stm32", "esp32", "arduino",
    ]),
    ("advanced-iot", "Advanced IoT", [
        "basic-ml-iot", "iot-hardware", "iot-cloud", "iot-projects", "mqtt", "computer-vision-iot", "raspberry-pi",
        "esp32", "arduino", "advanced-components", "tinyml",
    ]),
    ("database-technologies", "Database Technologies", ["mysql", "sql-server", "mongodb", "firebase"]),
    ("firebase-development", "Firebase Development", ["firebase", "auth-jwt", "rest-api"]),
    ("matlab-simulation", "MATLAB & Simulation", ["basic-matlab", "simulation"]),
    ("java-enterprise-development", "Java Enterprise Development", [
        "java", "servlet-jsp", "spring", "spring-boot", "spring-mvc", "spring-security", "hibernate",
        "maven", "rest-api", "auth-jwt",
    ]),
    ("python-backend-engineering", "Python Backend Engineering", [
        "python", "advanced-python", "flask", "fastapi", "rest-api", "auth-jwt", "postman", "docker",
    ]),
    ("computer-vision-for-iot", "Computer Vision for IoT", [
        "computer-vision-iot", "computer-vision", "basic-ml-iot", "esp32", "raspberry-pi", "flask", "mqtt",
    ]),
    ("modular-courses", "Modular Courses", [
        "c", "c-programming", "c-programming-fundamentals-deprecated", "cpp", "java",
        "python", "advanced-python", "python-dsa", "html5", "css3", "bootstrap", "javascript", "jquery",
        "mysql", "sql-server", "selenium", "java-selenium", "flask", "fastapi",
        # django: not yet built — no source file to merge, listed for visibility only
    ]),
]


def main():
    # Render every track fully into memory first, so that no output file is
    # written to disk until all source reads are done. Several tracks read
    # from the same source course files, and one output slug ("computer-vision")
    # also happens to be a source course slug — writing incrementally would let
    # an earlier track's output clobber a later track's input.
    rendered = {}
    for out_slug, title, structure in TRACKS:
        rendered[out_slug] = render_track(title, structure)
        print(f"  [RENDER] {out_slug} ({len(rendered[out_slug])} chars)")

    for out_slug, content in rendered.items():
        out_path = SYLLABUS_DIR / f"{out_slug}.md"
        out_path.write_text(content, encoding="utf-8")
        print(f"  [WRITE] {out_path}")

    print(f"\nDone. Wrote {len(rendered)} track syllabus files.")


if __name__ == "__main__":
    main()
