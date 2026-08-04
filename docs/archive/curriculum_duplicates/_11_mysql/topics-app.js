// Basic App Logic for Separate Topic Pages

document.addEventListener('DOMContentLoaded', () => {
    const themeToggle = document.getElementById('themeToggle');
    const searchInput = document.getElementById('searchInput');
    const navList = document.getElementById('navList');
    const topicTitleHeader = document.getElementById('topicTitleHeader');

    // Get current topic slug from filename
    const filename = window.location.pathname.split('/').pop().replace('.html', '');
    let currentTopic = null;
    if (typeof navData !== 'undefined') {
        currentTopic = navData.find(topic => topic.slug === filename);
    }

    // Load Theme
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    // Render Navigation
    renderNavigation();

    // Theme Toggle
    themeToggle.onclick = () => {
        const current = document.documentElement.getAttribute('data-theme');
        const next = current === 'dark' ? 'light' : 'dark';
        document.documentElement.setAttribute('data-theme', next);
        localStorage.setItem('theme', next);
        updateThemeIcon(next);
    };

    function updateThemeIcon(theme) {
        themeToggle.textContent = theme === 'dark' ? '☀️' : '🌙';
    }

    function renderNavigation() {
        if (typeof navData === 'undefined') {
            console.error('navData is missing!');
            return;
        }

        navList.innerHTML = navData.map(topic => {
            const topicNumber = (topic.id + 1).toString().padStart(2, '0');
            const isActive = currentTopic && topic.id === currentTopic.id;
            return `
                <div class="nav-item ${isActive ? 'active' : ''}" onclick="window.location.href='${topic.slug}.html'">
                    <span class="topic-badge">${topicNumber}</span>
                    ${topic.title}
                </div>
            `;
        }).join('');
    }
});

window.filterNav = function () {
    const q = document.getElementById('searchInput').value.toLowerCase();
    const items = document.querySelectorAll('.nav-item');
    items.forEach(item => {
        if (item.innerText.toLowerCase().includes(q)) {
            item.style.display = 'flex';
        } else {
            item.style.display = 'none';
        }
    });
};

window.copyCode = function (btn) {
    const code = btn.closest('.code-block-container').querySelector('code').innerText;
    navigator.clipboard.writeText(code);
    btn.textContent = 'Copied!';
    setTimeout(() => btn.textContent = 'Copy', 2000);
};

// Make function globally available
window.toggleAnswer = function (id, btn) {
    const el = document.getElementById(id);
    if (!el) {
        console.error('Element not found:', id);
        return;
    }
    const isHidden = el.style.display === 'none';
    el.style.display = isHidden ? 'block' : 'none';
    btn.textContent = isHidden ? 'Hide Answer' : 'Show Answer';
};

// Event Delegation for dynamically added content
document.addEventListener('click', function (e) {
    const btn = e.target.closest('.toggle-btn');
    if (btn) {
        const id = btn.getAttribute('data-target');
        if (id) {
            window.toggleAnswer(id, btn);
        }
    }
});