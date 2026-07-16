document.addEventListener('DOMContentLoaded', () => {
    const topics = [
        { id: '_01_demo_page_', title: '01. Demo Page', desc: 'A comprehensive overview of all UI elements, layout components, and styles used throughout the application to ensure consistency.' },
        { id: '_02_java', title: '02. Java Prerequisites', desc: 'Essential Java concepts required for Selenium: Classes, Objects, Inheritance, Polymorphism, and Collections Framework.' },
        { id: '_03_intro___', title: '03. Introduction', desc: 'Understand the fundamentals of Automation Testing, why Selenium is the industry leader, and its core components.' },
        { id: '_04_web_driver_commands___', title: '04. WebDriver Commands', desc: 'Master the basic commands to interact with the browser: launch, close, navigate, and fetch page details.' },
        { id: '_05_auto_webdriver_manager___', title: '05. Auto WebDriver Manager', desc: 'Learn to use WebDriverManager to automatically manage browser driver binaries, avoiding manual setup.' },
        { id: '_06_chrome_options___', title: '06. Chrome Options', desc: 'Advanced Chrome browser configurations: Headless mode, Incognito, disabling extensions, and setting capabilities.' },
        { id: '_07_page_load_strategy___', title: '07. Page Load Strategy', desc: 'Control how Selenium waits for the page to load: Normal, Eager, and None strategies for performance optimization.' },
        { id: '_08_locators___', title: '08. Locators', desc: 'The heart of Selenium. Deep dive into ID, Name, ClassName, TagName, LinkText, CSS Selectors, and XPath.' },
        { id: 'ws_xpath', title: '09. XPath Practice', desc: 'A dedicated practice area to master complex XPath expressions with a rich mock application.' },
        { id: '_10_navigation___', title: '10. Navigation', desc: 'Handle browser history interaction: Back, Forward, Refresh, and navigating to new URLs dynamically.' },
        { id: '_11_basic_html_controls___', title: '11. Basic HTML Controls', desc: 'Interact with standard inputs: Text fields, Buttons, Radio Buttons, and Checkboxes using sendKeys and click.' },
        { id: '_12_advanced_html_controls___', title: '12. Advanced HTML Controls', desc: 'Handling complex UI elements like Date Pickers, Sliders, Color Pickers, and Ranges.' },
        { id: '_13_dropdown___', title: '13. Dropdown Handling', desc: 'Master the Select class to handle static dropdowns and custom logic for dynamic Bootstrap dropdowns.' },
        { id: '_14_waits_and_synchronization___', title: '14. Waits & Synchronization', desc: 'Solve synchronization issues using Implicit Wait, Explicit Wait (WebDriverWait), and Fluent Wait.' },
        { id: '_15_iframe_handling___', title: '15. iFrame Handling', desc: 'Working with elements inside iFrames. Strategies to switch to frame by ID, Name, and Index.' },
        { id: '_16_alerts_and_popups___', title: '16. Alerts & Popups', desc: 'Handling JavaScript Alerts, Confirms, and Prompts. Switching to Alert context to accept or dismiss.' },
        { id: '_17_drag_drop___', title: '17. Drag & Drop', desc: 'Using the Actions class to perform complex mouse gestures like Drag and Drop, Click and Hold.' },
        { id: '_18_keyboard_actions___', title: '18. Keyboard Actions', desc: 'Simulating physical keyboard presses: KeyDown, KeyUp, Chord keys (Copy/Paste), and special keys.' },
        { id: '_19_mouse_actions___', title: '19. Mouse Actions', desc: 'Advanced mouse interactions: Mouse Hover, Context Click (Right Click), Double Click using Actions class.' },
        { id: '_20_scrolling_page___', title: '20. Scrolling Page', desc: 'Techniques to scroll the webpage: Scroll to element, Scroll by coordinates, and Infinite scrolling using JS.' },
        { id: '_21_multi_select___', title: '21. Multi-Select', desc: 'Handling special multi-select dropdown lists: Selecting multiple options and deselecting them.' },
        { id: '_22_find_all_links___', title: '22. Find All Links', desc: 'Web Scraping technique: Extracting all hyperlinks from a page and validating broken links.' },
        { id: '_23_window_handling___', title: '23. Window Handling', desc: 'Working with multiple tabs and windows. Switching context using Window Handles.' },
        { id: '_24_file_upload_download___', title: '24. File Upload/Download', desc: 'Automating file uploads using sendKeys and Robot class, and handling file downloads.' },
        { id: '_25_screenshots___', title: '25. Screenshots', desc: 'Capturing evidence. Taking full page screenshots and element specific screenshots on failure.' },
        { id: '_26_common_selenium_exceptions___', title: '26. Common Exceptions', desc: 'Troubleshooting guide: Handling StaleElementReference, NoSuchElement, and Timeout Exceptions.' },
        { id: '_27_page_object_model___', title: '27. Page Object Model', desc: 'Architectural Pattern: Creating reusable, maintainable, and readable test automation frameworks.' },
        { id: '_28_testng___', title: '28. TestNG', desc: 'Next Generation Testing Framework. Annotations, Assertions, Data Providers, and Parallel Execution.' },
        { id: '_29_maven_and_project_structure___', title: '29. Maven Project Structure', desc: 'Build Automation: Managing dependencies, plugins, and standard project directory layout.' },
        { id: '_30_reports___', title: '30. Reports', desc: 'Generating professional HTML execution reports using ExtentReports and Allure.' },
        { id: '_31_extra___', title: '31. Extras', desc: 'Miscellaneous topics, best practices, and tips for Selenium interview preparation.' },
        { id: '_32_connect_with_local_host', title: '32. Connect Localhost', desc: 'Setting up and testing applications running on your local development server environment.' }
    ];

    // Selectors
    const landingPageContainer = document.getElementById('landing-page');
    const landingGrid = document.querySelector('.landing-grid'); // Changed selector
    const contentDisplay = document.getElementById('content-display');
    const sidebar = document.getElementById('sidebar');
    const mainContent = document.getElementById('main-content'); // Added this
    const topicList = document.getElementById('topic-list');
    const homeBtn = document.getElementById('home-btn');

    // Render Landing Page Cards
    function renderLandingPage() {
        if (!landingGrid) return;
        landingGrid.innerHTML = '';
        topics.forEach(topic => {
            const card = document.createElement('div');
            card.className = 'topic-card';
            card.innerHTML = `
                <h3>${topic.title}</h3>
                <p>${topic.desc}</p>
            `;
            card.addEventListener('click', () => {
                // Special handling: Open XPath Practice worksheet in same window
                if (topic.id === 'ws_xpath') {
                    window.location.href = 'worksheets/ws_01_xpath_basics.html';
                } else {
                    loadTopic(topic.id);
                }
            });
            landingGrid.appendChild(card);
        });
    }

    // Show Home (Landing Page)
    function showHome(updateHash = true) {
        landingPageContainer.classList.remove('hidden');
        landingPageContainer.style.display = 'block';
        contentDisplay.classList.add('hidden');
        sidebar.classList.add('hidden');
        contentDisplay.innerHTML = '';
        if (updateHash) window.location.hash = '';
    }

    // Show Topic Content
    function loadTopic(topicId, updateHash = true) {
        landingPageContainer.classList.add('hidden');
        landingPageContainer.style.display = 'none';
        contentDisplay.classList.remove('hidden');
        sidebar.classList.remove('hidden');

        contentDisplay.innerHTML = '<div style="text-align:center; padding:50px; color:#666;">Loading content...</div>';

        fetch(topicId === 'ws_xpath' ? `worksheets/ws_01_xpath_basics.html` : `content/${topicId}.html`)
            .then(response => {
                if (!response.ok) throw new Error('Content not found');
                return response.text();
            })
            .then(html => {
                // Special handling for full-width topics (like XPath Practice)
                if (topicId === 'ws_xpath') {
                    contentDisplay.classList.add('full-width');
                    mainContent.classList.add('no-scroll');
                } else {
                    contentDisplay.classList.remove('full-width');
                    mainContent.classList.remove('no-scroll');
                }

                // Extract only the content from #content-display div to avoid duplicating nav/sidebar
                const parser = new DOMParser();
                const doc = parser.parseFromString(html, 'text/html');
                const innerContent = doc.getElementById('content-display');

                if (innerContent) {
                    // Extract only the inner HTML to avoid duplicating the full page structure
                    contentDisplay.innerHTML = innerContent.innerHTML;
                } else {
                    // Fallback if #content-display doesn't exist (e.g., worksheets)
                    contentDisplay.innerHTML = html;
                }

                window.scrollTo(0, 0);
                generateSidebarSubtopics();
                renderNavButtons(topicId); // Add nav buttons
                if (updateHash) window.location.hash = topicId;
            })
            .catch(error => {
                contentDisplay.innerHTML = `
                    <h1>Topic Under Construction</h1>
                    <p>The content for <strong>${topicId}</strong> is currently being written.</p>
                    <p>Please check back later.</p>
                `;
                console.error('Error loading topic:', error);
                if (updateHash) window.location.hash = topicId;
            });
    }

    // Generate Sidebar Subtopics
    function generateSidebarSubtopics() {
        topicList.innerHTML = '';
        const subtopics = contentDisplay.querySelectorAll('h2');

        if (subtopics.length === 0) {
            const li = document.createElement('li');
            li.innerHTML = '<span style="padding:15px 20px; display:block; color:#666;">No Subtopics</span>';
            topicList.appendChild(li);
            return;
        }

        subtopics.forEach((header, index) => {
            if (!header.id) {
                header.id = `subtopic-${index}`;
            }

            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = `#${header.id}`;
            a.className = 'topic-link';
            a.textContent = header.innerText;

            a.addEventListener('click', (e) => {
                e.preventDefault();
                header.scrollIntoView({ behavior: 'smooth' });
                document.querySelectorAll('.topic-link').forEach(l => l.classList.remove('active'));
                a.classList.add('active');
            });

            li.appendChild(a);
            topicList.appendChild(li);
        });
    }

    // Render Navigation Buttons (Prev / Next)
    function renderNavButtons(currentTopicId) {
        const index = topics.findIndex(t => t.id === currentTopicId);
        if (index === -1) return;

        const prevTopic = index > 0 ? topics[index - 1] : null;
        const nextTopic = index < topics.length - 1 ? topics[index + 1] : null;

        const navContainer = document.createElement('div');
        navContainer.className = 'nav-buttons-container';

        // Prev Button
        if (prevTopic) {
            const prevBtn = document.createElement('button');
            prevBtn.className = 'btn-nav prev';
            prevBtn.innerHTML = `&larr; Previous: ${prevTopic.title.split('.')[1] || prevTopic.title}`; // Shorten title
            prevBtn.onclick = () => loadTopic(prevTopic.id);
            navContainer.appendChild(prevBtn);
        }

        // Next Button
        if (nextTopic) {
            const nextBtn = document.createElement('button');
            nextBtn.className = 'btn-nav next';
            nextBtn.innerHTML = `Next: ${nextTopic.title.split('.')[1] || nextTopic.title} &rarr;`;
            nextBtn.onclick = () => loadTopic(nextTopic.id);
            navContainer.appendChild(nextBtn);
        }

        contentDisplay.appendChild(navContainer);
    }

    // Home Button Event
    if (homeBtn) {
        homeBtn.addEventListener('click', showHome);
    }

    // Handle Routing
    function handleRouting() {
        const hash = window.location.hash.substring(1);
        if (hash) {
            // Check if it's a main topic
            if (topics.some(t => t.id === hash)) {
                loadTopic(hash, false);
            } else if (hash.startsWith('subtopic-')) {
                // It's a subtopic anchor, handle if needed or let browser scroll if element exists
                // We don't want to reload the whole topic if just clicking subtopic
            }
        } else {
            showHome(false);
        }
    }

    // Listen for back/forward navigation
    window.addEventListener('hashchange', handleRouting);

    // Initialize
    renderLandingPage();
    handleRouting();
});
