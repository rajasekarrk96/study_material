-- =========================================================================
-- EduSphere Learning OS - Development Tools Category & Subject Seeding SQL
-- =========================================================================

-- 1. Insert Category: Development Tools
INSERT INTO categories (name, slug, type, description, icon, color, sort_order, is_active, created_at, updated_at)
VALUES (
    'Development Tools',
    'development-tools',
    'technical',
    'Essential tooling for software development lifecycle, source control, collaboration, and continuous integration.',
    'fas fa-tools',
    '#4f46e5',
    10,
    1,
    NOW(),
    NOW()
) ON DUPLICATE KEY UPDATE updated_at = NOW();

-- Get Category ID for referenced inserts
SET @cat_id = (SELECT id FROM categories WHERE slug = 'development-tools' LIMIT 1);

-- 2. Insert Subjects: Git, GitHub, GitLab
INSERT INTO subjects (category_id, name, slug, description, icon, logo_url, difficulty_level, sort_order, is_active, created_at, updated_at)
VALUES 
(
    @cat_id,
    'Git',
    'git',
    'Distributed version control fundamentals, branching mechanics, and local workspace management.',
    'fab fa-git-alt',
    '',
    'beginner',
    1,
    1,
    NOW(),
    NOW()
),
(
    @cat_id,
    'GitHub',
    'github',
    'Remote code hosting, pull request workflows, branch protections, and Actions pipelines.',
    'fab fa-github',
    '',
    'intermediate',
    2,
    1,
    NOW(),
    NOW()
),
(
    @cat_id,
    'GitLab',
    'gitlab',
    'DevOps lifecycle management, GitLab CI/CD, issue trackers, and registry integrations.',
    'fab fa-gitlab',
    '',
    'intermediate',
    3,
    1,
    NOW(),
    NOW()
) ON DUPLICATE KEY UPDATE updated_at = NOW();

-- Get Subject IDs
SET @sub_git_id = (SELECT id FROM subjects WHERE slug = 'git' LIMIT 1);
SET @sub_github_id = (SELECT id FROM subjects WHERE slug = 'github' LIMIT 1);
SET @sub_gitlab_id = (SELECT id FROM subjects WHERE slug = 'gitlab' LIMIT 1);

-- 3. Insert Courses
INSERT INTO courses (subject_id, title, slug, description, long_description, thumbnail_url, difficulty_level, status, language, estimated_hours, is_free, is_featured, published_at, created_at, updated_at)
VALUES
(
    @sub_git_id,
    'Git Fundamentals',
    'git-fundamentals',
    'Master local file tracking, basic snapshots, history inspects, and clean branching.',
    '<p>This course teaches you Git internals and workflow best practices from the ground up.</p>',
    '',
    'beginner',
    'published',
    'en',
    15,
    1,
    1,
    NOW(),
    NOW(),
    NOW()
),
(
    @sub_github_id,
    'GitHub Essentials',
    'github-essentials',
    'Manage remote repos, collaborate with Pull Requests, and customize repositories.',
    '<p>Essential developer skills for collaborative coding and code review workflows.</p>',
    '',
    'intermediate',
    'published',
    'en',
    10,
    1,
    1,
    NOW(),
    NOW(),
    NOW()
),
(
    @sub_gitlab_id,
    'GitLab Basics',
    'gitlab-basics',
    'Manage GitLab project groups, boards, and standard Merge Requests.',
    '<p>Learn how to use GitLab as a complete, single-application software suite.</p>',
    '',
    'intermediate',
    'published',
    'en',
    10,
    1,
    1,
    NOW(),
    NOW(),
    NOW()
) ON DUPLICATE KEY UPDATE updated_at = NOW();
