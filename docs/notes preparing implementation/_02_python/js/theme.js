/**
 * EduSphere Theme Switcher
 * Handles light/dark theme toggling with localStorage persistence
 */

(function () {
    'use strict';

    const THEME_KEY = 'edusphere-theme';
    const THEME_LIGHT = 'light';
    const THEME_DARK = 'dark';

    /**
     * Get the current theme from localStorage or system preference
     */
    function getCurrentTheme() {
        const savedTheme = localStorage.getItem(THEME_KEY);

        if (savedTheme) {
            return savedTheme;
        }

        // Check system preference
        if (window.matchMedia && window.matchMedia('(prefers-color-scheme: dark)').matches) {
            return THEME_DARK;
        }

        return THEME_LIGHT;
    }

    /**
     * Apply theme to the document
     */
    function applyTheme(theme) {
        document.documentElement.setAttribute('data-theme', theme);
        localStorage.setItem(THEME_KEY, theme);

        // Update theme toggle button icon
        updateThemeToggleIcon(theme);
    }

    /**
     * Update the theme toggle button aria-label
     */
    function updateThemeToggleIcon(theme) {
        const themeToggle = document.getElementById('theme-toggle');
        if (!themeToggle) return;

        // Update accessibility labels only (icons are always visible in the sliding toggle)
        if (theme === THEME_DARK) {
            themeToggle.setAttribute('aria-label', 'Switch to light mode');
            themeToggle.setAttribute('title', 'Switch to light mode');
        } else {
            themeToggle.setAttribute('aria-label', 'Switch to dark mode');
            themeToggle.setAttribute('title', 'Switch to dark mode');
        }
    }

    /**
     * Toggle between light and dark themes
     */
    function toggleTheme() {
        const currentTheme = getCurrentTheme();
        const newTheme = currentTheme === THEME_LIGHT ? THEME_DARK : THEME_LIGHT;

        // Add transition class to body for smooth theme change
        document.body.style.transition = 'background-color 300ms ease, color 300ms ease';

        applyTheme(newTheme);

        // Remove transition after animation
        setTimeout(() => {
            document.body.style.transition = '';
        }, 300);

        // Dispatch custom event for other scripts to listen to
        window.dispatchEvent(new CustomEvent('themechange', {
            detail: { theme: newTheme }
        }));
    }

    /**
     * Initialize theme on page load
     */
    function initTheme() {
        const theme = getCurrentTheme();
        applyTheme(theme);

        // Set up theme toggle button
        const themeToggle = document.getElementById('theme-toggle');
        if (themeToggle) {
            themeToggle.addEventListener('click', toggleTheme);
        }

        // Listen for system theme changes
        if (window.matchMedia) {
            window.matchMedia('(prefers-color-scheme: dark)').addEventListener('change', (e) => {
                // Only auto-switch if user hasn't manually set a preference
                const savedTheme = localStorage.getItem(THEME_KEY);
                if (!savedTheme) {
                    const newTheme = e.matches ? THEME_DARK : THEME_LIGHT;
                    applyTheme(newTheme);
                }
            });
        }
    }

    // Initialize theme as soon as possible to prevent flash
    if (document.readyState === 'loading') {
        document.addEventListener('DOMContentLoaded', initTheme);
    } else {
        initTheme();
    }

    // Export functions for external use if needed
    window.EduSphereTheme = {
        toggle: toggleTheme,
        set: applyTheme,
        get: getCurrentTheme
    };
})();
