/* Learning OS — main.js
   Handles: theme, flash auto-dismiss, stats counter animation
*/
"use strict";

// ── AUTO-DISMISS FLASH MESSAGES ───────────────────────────────
document.querySelectorAll('.flash').forEach(el => {
    setTimeout(() => {
        el.style.opacity = '0';
        el.style.transform = 'translateX(100%)';
        setTimeout(() => el.remove(), 300);
    }, 4000);
});

// ── ANIMATED COUNTERS (stats bar) ────────────────────────────
function animateCounter(el, target, duration = 1200) {
    const start = performance.now();
    const update = (now) => {
        const elapsed = now - start;
        const progress = Math.min(elapsed / duration, 1);
        const ease = 1 - Math.pow(1 - progress, 3);
        el.textContent = Math.floor(ease * target).toLocaleString();
        if (progress < 1) requestAnimationFrame(update);
    };
    requestAnimationFrame(update);
}

// Fetch live stats from API and animate
async function loadStats() {
    try {
        const res = await fetch('/api/v1/stats');
        if (!res.ok) return;
        const data = await res.json();
        const map = {
            'stat-courses': data.courses ?? 0,
            'stat-lessons': data.lessons ?? 0,
            'stat-topics':  data.topics  ?? 0,
            'stat-sources': data.sources ?? 0,
        };
        Object.entries(map).forEach(([id, val]) => {
            const el = document.getElementById(id);
            if (el) animateCounter(el, val);
        });
    } catch (_) {}
}

if (document.getElementById('stat-courses')) loadStats();

// ── MOBILE SIDEBAR OVERLAY CLOSE ─────────────────────────────
document.addEventListener('click', (e) => {
    const sidebar = document.getElementById('lesson-sidebar');
    const toggle  = document.getElementById('sidebar-toggle');
    if (sidebar && sidebar.classList.contains('open') &&
        !sidebar.contains(e.target) && e.target !== toggle) {
        sidebar.classList.remove('open');
    }
});

// ── COURSES DROPDOWN INTERACTION ─────────────────────────────
document.addEventListener('DOMContentLoaded', () => {
    const dropdownBtn = document.getElementById('courses-dropdown-btn');
    const dropdownMenu = document.getElementById('courses-dropdown-menu');
    const dropdownContainer = dropdownBtn ? dropdownBtn.parentElement : null;

    if (dropdownBtn && dropdownMenu) {
        dropdownBtn.addEventListener('click', (e) => {
            e.stopPropagation();
            dropdownMenu.classList.toggle('show');
            if (dropdownContainer) {
                dropdownContainer.classList.toggle('open');
            }
        });

        // Close dropdown when clicking outside
        document.addEventListener('click', (e) => {
            if (dropdownContainer && !dropdownContainer.contains(e.target)) {
                dropdownMenu.classList.remove('show');
                dropdownContainer.classList.remove('open');
            }
        });
    }
});

