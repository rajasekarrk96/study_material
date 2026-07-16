// DOM Elements
const navList = document.getElementById('navList');
const contentArea = document.getElementById('contentArea');
const currentTopicName = document.getElementById('currentTopicName');
const searchInput = document.getElementById('searchInput');
const themeToggle = document.getElementById('themeToggle');
const menuToggle = document.getElementById('menuToggle');
const sidebar = document.querySelector('.sidebar');

// Initialize
function init() {
    renderNavigation(navData);

    // Load Theme Preference
    const savedTheme = localStorage.getItem('theme') || 'light';
    document.documentElement.setAttribute('data-theme', savedTheme);
    updateThemeIcon(savedTheme);

    // Logo Action - go to first topic
    document.getElementById('brandLogo').onclick = () => {
        window.location.href = 'topics/01_introduction.html';
    };
}

// Render Navigation
function renderNavigation(topics) {
    if (typeof navData === 'undefined') {
        console.error("navData is undefined. Make sure nav.js is loaded.");
        return;
    }

    navList.innerHTML = '';

    topics.forEach(note => {
        const item = document.createElement('div');
        // Check if we are on a topic page or just on index
        // Since this is index.html (mostly), no active topic usually, OR we could make index redirect to topic-0?
        // Let's keep index as a landing page or just a list.
        // For now, no 'active' class logic needed unless we parse URL.

        item.className = 'nav-item';

        item.onclick = () => {
            window.location.href = `topics/${note.slug}.html`;
        };

        const topicNumber = (note.id + 1).toString().padStart(2, '0');

        item.innerHTML = `
            <span class="topic-badge">${topicNumber}</span>
            <span>${note.title}</span>
        `;

        navList.appendChild(item);
    });
}

// Search Functionality
searchInput.addEventListener('input', (e) => {
    const term = e.target.value.toLowerCase();
    const filtered = navData.filter(note => note.title.toLowerCase().includes(term));
    renderNavigation(filtered);
});

// Theme Toggle
themeToggle.addEventListener('click', () => {
    const current = document.documentElement.getAttribute('data-theme');
    const next = current === 'dark' ? 'light' : 'dark';
    document.documentElement.setAttribute('data-theme', next);
    localStorage.setItem('theme', next);
    updateThemeIcon(next);
});

function updateThemeIcon(theme) {
    if (theme === 'dark') {
        themeToggle.textContent = '☀️';
    } else {
        themeToggle.textContent = '🌙';
    }
}

// Mobile Menu
menuToggle.addEventListener('click', () => {
    sidebar.classList.toggle('collapsed');
});

// Start
init();
