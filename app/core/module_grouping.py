"""
Learning OS — Module grouping helper for syllabus generation.
Historical re-ingestion left many courses with multiple module rows sharing
the same sort_order/number: sometimes the same module written twice with
slightly different title wording (a true duplicate, safe to merge), and
sometimes genuinely distinct modules that were all mis-numbered "1" by a
buggy ingestion script (must be kept apart and renumbered).
"""
import re

_NUMBERED_MODULE_PREFIX_RE = re.compile(r"^module\s*\d+\s*[:.\-—]\s*", re.IGNORECASE)


def _strip_numbered_prefix(title: str) -> str:
    return _NUMBERED_MODULE_PREFIX_RE.sub("", title).strip().lower()


def _similar(title_a: str, title_b: str) -> bool:
    """True only if these look like the *same* module written twice by two
    different ingestion passes, not merely a related topic.

    The reliable signal, found by checking against real duplicate pairs, is
    a "Module N: " *numbered* prefix present on exactly one of the two
    titles — that's the fingerprint of one ingestion pass's branding applied
    to what both times was the same conceptual module (e.g. "Docker
    Fundamentals" / "Module 1: Docker Fundamentals").

    Generic word-overlap scoring was tried and rejected: shared domain
    vocabulary (e.g. "git" or "module" itself appearing in every title of a
    course) produced false-positive merges of genuinely distinct modules
    that had just been mis-numbered identically by a buggy ingestion script
    (e.g. Git Fundamentals' 8 unrelated modules all stamped sort_order=1).
    """
    a_numbered = bool(_NUMBERED_MODULE_PREFIX_RE.match(title_a))
    b_numbered = bool(_NUMBERED_MODULE_PREFIX_RE.match(title_b))

    if a_numbered != b_numbered:
        return True

    if a_numbered and b_numbered:
        core_a, core_b = _strip_numbered_prefix(title_a), _strip_numbered_prefix(title_b)
        return core_a == core_b or core_a in core_b or core_b in core_a

    return title_a.strip().lower() == title_b.strip().lower()


def group_modules(module_groups: list) -> list:
    """
    module_groups: list of (module_number, module_title, [lesson, ...]) in
    original db/file order, one entry per raw module row.

    Returns: list of (display_number, display_title, [lesson, ...]) with
    true duplicates merged (lessons concatenated, de-duplicated by title,
    under whichever title is more descriptive) and mis-numbered distinct
    modules renumbered sequentially.
    """
    by_number = {}
    order = []
    for num, title, lessons in module_groups:
        if num not in by_number:
            by_number[num] = []
            order.append(num)
        by_number[num].append((title, lessons))

    result = []
    next_number = 1
    for num in order:
        groups = by_number[num]
        if len(groups) == 1:
            title, lessons = groups[0]
            result.append((next_number, title, lessons))
            next_number += 1
            continue

        # Multiple module rows share this number — cluster them by title similarity.
        clusters = []  # list of [ (title, lessons), ... ]
        for title, lessons in groups:
            placed = False
            for cluster in clusters:
                if _similar(cluster[0][0], title):
                    cluster.append((title, lessons))
                    placed = True
                    break
            if not placed:
                clusters.append([(title, lessons)])

        for cluster in clusters:
            if len(cluster) == 1:
                title, lessons = cluster[0]
                result.append((next_number, title, lessons))
            else:
                # True duplicate: merge lessons, keep the longer/more
                # descriptive title, dedupe lessons by title.
                best_title = max((t for t, _ in cluster), key=len)
                seen_titles = set()
                merged_lessons = []
                for _, lessons in cluster:
                    for lesson in lessons:
                        lesson_title = lesson[0] if isinstance(lesson, tuple) else lesson["title"]
                        if lesson_title in seen_titles:
                            continue
                        seen_titles.add(lesson_title)
                        merged_lessons.append(lesson)
                result.append((next_number, best_title, merged_lessons))
            next_number += 1

    return result
