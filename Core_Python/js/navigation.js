// Navigation toggle and smooth scroll functionality
document.addEventListener('DOMContentLoaded', function () {
    // Inject Toggle Button into Logo Container
    const logoContainer = document.querySelector('.logo');
    if (logoContainer && !document.querySelector('.toggle-btn')) {
        const toggleBtn = document.createElement('button');
        toggleBtn.className = 'toggle-btn';
        toggleBtn.innerHTML = '<i class="fas fa-bars"></i>';
        logoContainer.insertBefore(toggleBtn, logoContainer.firstChild);

        toggleBtn.addEventListener('click', function () {
            document.body.classList.toggle('sidebar-hidden');
        });

        // Auto-hide sidebar on mobile devices
        if (window.innerWidth < 992) {
            document.body.classList.add('sidebar-hidden');
        }
    }
    // Toggle dropdown navigation
    const navItemsWithSubtopics = document.querySelectorAll('.nav-item.has-subtopics > a');

    navItemsWithSubtopics.forEach(item => {
        item.addEventListener('click', function (e) {
            // Only prevent default if clicking on the same page
            const href = this.getAttribute('href');
            const currentPage = window.location.pathname.split('/').pop();

            if (href === currentPage || href === '#') {
                e.preventDefault();
            }

            const parentItem = this.parentElement;
            const wasExpanded = parentItem.classList.contains('expanded');

            // Close all other expanded items
            document.querySelectorAll('.nav-item.has-subtopics').forEach(navItem => {
                if (navItem !== parentItem) {
                    navItem.classList.remove('expanded');
                }
            });

            // Toggle current item
            parentItem.classList.toggle('expanded');
        });
    });

    // Smooth scroll to sections with optimized offset
    const subtopicLinks = document.querySelectorAll('.sub-nav a');

    subtopicLinks.forEach(link => {
        link.addEventListener('click', function (e) {
            const href = this.getAttribute('href');

            // Check if it's an anchor link
            if (href && href.startsWith('#')) {
                e.preventDefault();
                const targetId = href.substring(1);
                const targetElement = document.getElementById(targetId);

                if (targetElement) {
                    // Calculate offset for better positioning (accounts for fixed headers)
                    const offset = 80; // Adjust this value based on your header height
                    const elementPosition = targetElement.getBoundingClientRect().top;
                    const offsetPosition = elementPosition + window.pageYOffset - offset;

                    // Smooth scroll to target with optimized behavior
                    window.scrollTo({
                        top: offsetPosition,
                        behavior: 'smooth'
                    });

                    // Update active state
                    document.querySelectorAll('.sub-nav li').forEach(li => {
                        li.classList.remove('active');
                    });
                    this.parentElement.classList.add('active');

                    // Update URL hash without jumping
                    history.pushState(null, null, href);
                }
            }
        });
    });

    // Highlight active subtopic on scroll with debouncing for better performance
    let scrollTimeout;
    const observerOptions = {
        threshold: [0, 0.25, 0.5, 0.75, 1],
        rootMargin: '-80px 0px -50% 0px'
    };

    const observer = new IntersectionObserver((entries) => {
        clearTimeout(scrollTimeout);
        scrollTimeout = setTimeout(() => {
            entries.forEach(entry => {
                if (entry.isIntersecting && entry.intersectionRatio > 0.25) {
                    const id = entry.target.getAttribute('id');
                    if (id) {
                        document.querySelectorAll('.sub-nav li').forEach(li => {
                            li.classList.remove('active');
                        });
                        const activeLink = document.querySelector(`.sub-nav a[href="#${id}"]`);
                        if (activeLink) {
                            activeLink.parentElement.classList.add('active');
                        }
                    }
                }
            });
        }, 100); // Debounce delay
    }, observerOptions);

    // Observe all sections with IDs
    document.querySelectorAll('[id]').forEach(section => {
        if (section.tagName === 'H2' || section.tagName === 'H3') {
            observer.observe(section);
        }
    });

    // Auto-expand current page's navigation
    const currentPage = window.location.pathname.split('/').pop();
    const currentNavLink = document.querySelector(`.nav-item.has-subtopics a[href="${currentPage}"]`);
    if (currentNavLink) {
        currentNavLink.parentElement.classList.add('expanded');
    }

    // Handle hash on page load
    if (window.location.hash) {
        setTimeout(() => {
            const targetElement = document.querySelector(window.location.hash);
            if (targetElement) {
                const offset = 80;
                const elementPosition = targetElement.getBoundingClientRect().top;
                const offsetPosition = elementPosition + window.pageYOffset - offset;

                window.scrollTo({
                    top: offsetPosition,
                    behavior: 'smooth'
                });
            }
        }, 300); // Delay to ensure page is fully loaded
    }
});
