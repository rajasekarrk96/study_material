# 13 — Recommendation Engine

> The Recommendation Engine creates user profiles, checks learning trajectories, and recommends courses, tags, and revision paths.

---

## 13.1 Rule-Based vs. Vector Similarity Recommendations

```
                              ┌────────────────────────┐
                              │ Recommendation Models  │
                              └───────────┬────────────┘
                                          │
                ┌─────────────────────────┴─────────────────────────┐
                ▼                                                   ▼
 ┌─────────────────────────────┐                     ┌─────────────────────────────┐
 │    Rule-Based Filtering     │                     │     Vector Embeddings       │
 ├─────────────────────────────┤                     ├─────────────────────────────┤
 │ Prerequisite chains,        │                     │ cosine similarity matching  │
 │ current course trajectory   │                     │ user history interests vs   │
 │ and tag taxonomy matches.   │                     │ course topic vectors.       │
 └─────────────────────────────┘                     └─────────────────────────────┘
```

---

## 13.2 Collaborative Recommendation Services

The platform utilizes content similarity matching to recommend paths if a user has completed a course or topic tag sequence.

```python
# app/services/recommendation_service.py

import math
from app.domains.content.models import Course, Tag

class RecommendationEngine:
    def __init__(self, db_session):
        self.db = db_session

    def get_recommended_courses(self, user_id: int, limit: int = 5) -> list[Course]:
        """
        Recommends next courses based on completed topics, prerequisites, and vector similarity profiles.
        """
        # 1. Retrieve user's completed courses
        # 2. Extract tags matching high performance (passed quizzes/exercises)
        # 3. Retrieve new courses satisfying prerequisite criteria
        # 4. Score eligible courses using content overlap (cosine similarity of tag sets)
        
        user_completed_ids = self._get_user_completed_course_ids(user_id)
        user_tags = self._get_user_interests_tags(user_id)
        
        all_courses = self.db.query(Course).filter(
            Course.status == 'published',
            ~Course.id.in_(user_completed_ids)
        ).all()
        
        scored_courses = []
        for course in all_courses:
            # Check prerequisites
            if not self._prereqs_satisfied(user_id, course):
                continue
                
            course_tags = [t.name for t in course.tags]
            score = self._cosine_similarity(user_tags, course_tags)
            scored_courses.append((course, score))
            
        # Sort courses descending by similarity score
        scored_courses.sort(key=lambda x: x[1], reverse=True)
        return [item[0] for item in scored_courses[:limit]]

    def _cosine_similarity(self, list1: list[str], list2: list[str]) -> float:
        set1, set2 = set(list1), set(list2)
        intersection = len(set1.intersection(set2))
        denominator = math.sqrt(len(set1) * len(set2))
        return intersection / denominator if denominator > 0 else 0.0

    def _get_user_completed_course_ids(self, user_id: int) -> list[int]:
        # Placeholder database check
        return []

    def _get_user_interests_tags(self, user_id: int) -> list[str]:
        # Returns tags of courses student spent most time on or passed
        return ["python", "basics"]

    def _prereqs_satisfied(self, user_id: int, course: Course) -> bool:
        # Evaluate course prerequisites
        return True
```
