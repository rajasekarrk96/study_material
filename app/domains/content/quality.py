"""
Learning OS — Content Quality & Readability Metrics.
Calculates Flesch Reading Ease readability scores and simulates plagiarism audits.
"""
import re
from app.core.extensions import db
from app.domains.content.models import Lesson, ContentQualityScore


def count_syllables(word: str) -> int:
    """Helper method to estimate syllables in a word."""
    word = word.lower().strip()
    if not word:
        return 0
    # Remove punctuation
    word = re.sub(r"[^a-z]", "", word)
    if not word:
        return 0
    # Basic syllable rules
    vowels = "aeiouy"
    count = 0
    if word[0] in vowels:
        count += 1
    for index in range(1, len(word)):
        if word[index] in vowels and word[index - 1] not in vowels:
            count += 1
    # Handle silent 'e' at end
    if word.endswith("e"):
        count -= 1
    # Adjust for very short words
    if count == 0:
        count = 1
    return count


def calculate_flesch_reading_ease(text: str) -> float:
    """
    Computes the Flesch Reading Ease score.
    Formula: 206.835 - 1.015 * (words/sentences) - 84.6 * (syllables/words)
    """
    text = text.strip()
    if not text:
        return 100.0

    # Extract sentences
    sentences = [s for s in re.split(r"[.!?]+", text) if s.strip()]
    sentence_count = max(1, len(sentences))

    # Extract words
    words = [w for w in re.split(r"\s+", text) if w.strip()]
    word_count = max(1, len(words))

    # Calculate total syllables
    syllable_count = sum(count_syllables(w) for w in words)
    syllable_count = max(1, syllable_count)

    # Apply Flesch Reading Ease formula
    score = 206.835 - 1.015 * (word_count / sentence_count) - 84.6 * (syllable_count / word_count)
    return round(max(0.0, min(100.0, score)), 2)


def run_quality_check(lesson_id: int) -> ContentQualityScore:
    """
    Performs readability and plagiarism analysis for a lesson,
    saving the metrics to the content_quality_scores table.
    """
    lesson = db.session.get(Lesson, lesson_id)
    if not lesson:
        raise ValueError(f"Lesson {lesson_id} not found.")

    # Combine sections content
    full_text_list = []
    for section in lesson.sections:
        if section.content_markdown:
            full_text_list.append(section.content_markdown)
    full_text = " ".join(full_text_list)

    # Readability
    readability = calculate_flesch_reading_ease(full_text)

    # Plagiarism (mocked: check if sentences overlap with other lessons)
    plagiarism_percentage = 0.0
    if len(full_text) > 100:
        # Mock calculation: simulate 2.5% plagiarism for baseline verification
        plagiarism_percentage = 2.5

    feedback = []
    if readability < 30.0:
        feedback.append("Very difficult to read. Recommend simplifying sentences.")
    elif readability < 50.0:
        feedback.append("Difficult to read. Suitable for college level.")
    elif readability > 90.0:
        feedback.append("Very easy to read. Excellent for beginners.")
    else:
        feedback.append("Good readability level.")

    if plagiarism_percentage > 10.0:
        feedback.append("Warning: High matching overlap detected.")

    quality_score = ContentQualityScore(
        lesson_id=lesson.id,
        readability_score=readability,
        plagiarism_percentage=plagiarism_percentage,
        automated_feedback=" | ".join(feedback)
    )
    db.session.add(quality_score)
    db.session.commit()
    return quality_score
