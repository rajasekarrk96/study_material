"""
Learning OS — Sitemap Generator.
Generates a standard sitemap.xml dynamically containing all published courses and lessons.
Saves the output sitemap directly to app/static/sitemap.xml.
"""
import os
import xml.etree.ElementTree as ET
from datetime import datetime
from flask import current_app, url_for
from app.domains.content.models import Course, Lesson


def generate_sitemap_xml() -> str:
    """
    Generates a sitemap.xml structure for SEO crawlers.
    Returns the raw XML string and writes it to app/static/sitemap.xml.
    """
    root = ET.Element("urlset", xmlns="http://www.sitemaps.org/schemas/sitemap/0.9")

    # Base URL (default fallback to local/prod domain check)
    base_url = "https://bytesandboards.com"

    # Add homepage
    url_el = ET.SubElement(root, "url")
    ET.SubElement(url_el, "loc").text = f"{base_url}/"
    ET.SubElement(url_el, "lastmod").text = datetime.utcnow().strftime("%Y-%m-%d")
    ET.SubElement(url_el, "changefreq").text = "daily"
    ET.SubElement(url_el, "priority").text = "1.0"

    # Add Catalog
    url_el = ET.SubElement(root, "url")
    ET.SubElement(url_el, "loc").text = f"{base_url}/catalog"
    ET.SubElement(url_el, "lastmod").text = datetime.utcnow().strftime("%Y-%m-%d")
    ET.SubElement(url_el, "changefreq").text = "weekly"
    ET.SubElement(url_el, "priority").text = "0.8"

    # Add all courses
    courses = Course.query.filter_by(status="published", is_deleted=False).all()
    for course in courses:
        url_el = ET.SubElement(root, "url")
        # In flask context, we can construct the paths manually to avoid requiring active requests context
        ET.SubElement(url_el, "loc").text = f"{base_url}/learn/{course.slug}/"
        ET.SubElement(url_el, "lastmod").text = (course.updated_at or datetime.utcnow()).strftime("%Y-%m-%d")
        ET.SubElement(url_el, "changefreq").text = "weekly"
        ET.SubElement(url_el, "priority").text = "0.7"

        # Add all lessons in this course
        for module in course.modules:
            for lesson in module.lessons:
                if not lesson.is_deleted and lesson.status == "published":
                    url_el = ET.SubElement(root, "url")
                    ET.SubElement(url_el, "loc").text = f"{base_url}/learn/{course.slug}/{module.slug}/{lesson.slug}/"
                    ET.SubElement(url_el, "lastmod").text = (lesson.updated_at or datetime.utcnow()).strftime("%Y-%m-%d")
                    ET.SubElement(url_el, "changefreq").text = "weekly"
                    ET.SubElement(url_el, "priority").text = "0.6"

    # Convert to string with proper XML declarations
    xml_str = ET.tostring(root, encoding="utf-8", method="xml")
    xml_header = b'<?xml version="1.0" encoding="UTF-8"?>\n'
    full_xml = xml_header + xml_str

    # Write file out safely to static/sitemap.xml
    static_dir = os.path.join(current_app.root_path, "static")
    os.makedirs(static_dir, exist_ok=True)
    sitemap_path = os.path.join(static_dir, "sitemap.xml")
    
    with open(sitemap_path, "wb") as f:
        f.write(full_xml)

    return full_xml.decode("utf-8")
