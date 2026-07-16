# 18 — SEO Strategy

> The SEO Strategy ensures courses and public lessons rank effectively on search engines.

---

## 18.1 Key Pillars

```
             ┌─────────────────────────┐
             │       SEO Strategy      │
             └────────────┬────────────┘
                          │
         ┌────────────────┴────────────────┐
         ▼                                 ▼
┌──────────────────┐             ┌──────────────────┐
│   Structured     │             │    Metadata      │
│  Schema Markup   │             │   Management     │
├──────────────────┤             ├──────────────────┤
│ schema.org JSON- │             │ Canonical URLs,  │
│ LD injections on │             │ OpenGraph cards, │
│ lesson templates │             │ custom meta tags │
└──────────────────┘             └──────────────────┘
```

---

## 18.2 Structured Schema Injection (schema.org)

For courses, lessons, and Q&A (interview questions), Jinja2 templates inject JSON-LD context payloads dynamically:

```html
<!-- For Course Overview Pages -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "Course",
  "name": "{{ course.title }}",
  "description": "{{ course.description }}",
  "provider": {
    "@type": "Organization",
    "name": "Learning OS",
    "sameAs": "https://www.learningos.com"
  },
  "hasCourseInstance": {
    "@type": "CourseInstance",
    "courseMode": "Online",
    "instructor": {
      "@type": "Person",
      "name": "{{ course.author.display_name }}"
    }
  }
}
</script>
```

```html
<!-- For Lesson Pages -->
<script type="application/ld+json">
{
  "@context": "https://schema.org",
  "@type": "TechArticle",
  "headline": "{{ lesson.title }}",
  "description": "{{ lesson.summary }}",
  "inLanguage": "en",
  "articleBody": "{{ lesson.sections['overview'].content_markdown | truncate(300) }}",
  "author": {
    "@type": "Person",
    "name": "{{ lesson.author.display_name }}"
  }
}
</script>
```

---

## 18.3 Automated Sitemaps Generator

Every night, a background worker updates the `sitemap.xml` file. It iterates over published paths, courses, and lessons, appending priority tags based on content hierarchy:

| Page Type | Change Frequency | Priority |
|-----------|------------------|----------|
| Home Page | Daily            | 1.0      |
| Course Page | Weekly         | 0.8      |
| Lesson Page | Monthly        | 0.7      |

---

## 18.4 URL Redirects Policy (Slug Updates)
If an editor updates a lesson slug, the database registers a redirect record mapping `old_slug` to `new_slug`. The routing middleware intercepts these requests and responds with a `301 Moved Permanently` redirect to preserve indexing rank.
