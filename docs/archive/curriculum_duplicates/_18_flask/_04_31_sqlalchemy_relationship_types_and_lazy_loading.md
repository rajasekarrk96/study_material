# SQLAlchemy Relationship Types and Lazy Loading

> **Course**: Flask | **Module**: Advanced Flask Patterns | **Difficulty**: advanced

---

### 1. One-to-Many Relationship
```python
class Author(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    name = db.Column(db.String(100))
    books = db.relationship('Book', back_populates='author',
                            lazy='dynamic', cascade='all, delete-orphan')

class Book(db.Model):
    id = db.Column(db.Integer, primary_key=True)
    title = db.Column(db.String(200))
    author_id = db.Column(db.Integer, db.ForeignKey('author.id'))
    author = db.relationship('Author', back_populates='books')
```

### 2. Many-to-Many with Association Table
```python
# Association table (no model needed for simple junction)
student_course = db.Table('student_course',
    db.Column('student_id', db.Integer, db.ForeignKey('student.id')),
    db.Column('course_id', db.Integer, db.ForeignKey('course.id'))
)

class Student(db.Model):
    courses = db.relationship('Course', secondary=student_course,
                              back_populates='students')
```

### 3. Lazy Loading Strategies
| Strategy | SQL | When |
|---|---|---|
| `lazy='select'` | Separate SELECT on access | Default, small sets |
| `lazy='joined'` | JOIN in same query | Always needed |
| `lazy='subquery'` | Subquery per collection | Medium sets |
| `lazy='dynamic'` | Returns Query object | Large collections |
| `lazy='raise'` | Raises error if accessed | Detect N+1 |

```python
# Eager loading to avoid N+1
authors = Author.query.options(
    db.joinedload(Author.books)
).all()

# Using selectin for collections
authors = Author.query.options(
    db.selectinload(Author.books)
).all()
```

### 4. Association Object Pattern (with extra fields)
```python
class Enrollment(db.Model):
    student_id = db.Column(db.Integer, db.ForeignKey('student.id'), primary_key=True)
    course_id  = db.Column(db.Integer, db.ForeignKey('course.id'), primary_key=True)
    enrolled_at = db.Column(db.DateTime, default=datetime.utcnow)
    grade = db.Column(db.Float)
    student = db.relationship('Student', back_populates='enrollments')
    course  = db.relationship('Course',  back_populates='enrollments')
```

---

Build a Blog API with Authors → Posts (one-to-many) and Posts ↔ Tags (many-to-many). Use `selectinload` to return all posts with their tags in a single efficient query.

---
