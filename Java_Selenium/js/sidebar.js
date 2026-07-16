// Sidebar topics
const topics = [
    { id: '_01_demo_page_', title: '01. Demo Page', icon: 'fa-play-circle' },
    { id: '_02_java', title: '02. Java Prerequisites', icon: 'fa-coffee' },
    { id: '_03_intro___', title: '03. Introduction', icon: 'fa-info-circle' },
    { id: '_04_web_driver_commands___', title: '04. WebDriver Commands', icon: 'fa-terminal' },
    { id: '_05_auto_webdriver_manager___', title: '05. WebDriver Setup', icon: 'fa-magic' },
    { id: '_06_chrome_options___', title: '06. Chrome Options', icon: 'fa-sliders-h' },
    { id: '_07_page_load_strategy___', title: '07. Page Load', icon: 'fa-hourglass-start' },
    { id: '_08_locators___', title: '08. Locators', icon: 'fa-crosshairs' },
    { id: '_10_navigation___', title: '10. Navigation', icon: 'fa-compass' },
    { id: '_11_basic_html_controls___', title: '11. Basic Controls', icon: 'fa-edit' },
    { id: '_12_advanced_html_controls___', title: '12. Advanced Controls', icon: 'fa-layer-group' },
    { id: '_13_dropdown___', title: '13. Dropdowns', icon: 'fa-list' },
    { id: '_14_waits_and_synchronization___', title: '14. Waits & Sync', icon: 'fa-clock' },
    { id: '_15_iframe_handling___', title: '15. Iframes', icon: 'fa-cube' },
    { id: '_16_alerts_and_popups___', title: '16. Alerts', icon: 'fa-exclamation-triangle' },
    { id: '_17_drag_drop___', title: '17. Drag & Drop', icon: 'fa-mouse-pointer' },
    { id: '_18_keyboard_actions___', title: '18. Keyboard', icon: 'fa-keyboard' },
    { id: '_19_mouse_actions___', title: '19. Mouse', icon: 'fa-mouse' },
    { id: '_20_scrolling_page___', title: '20. Scrolling', icon: 'fa-scroll' },
    { id: '_21_multi_select___', title: '21. Multi-Select', icon: 'fa-check-double' },
    { id: '_22_find_all_links___', title: '22. Find All Links', icon: 'fa-link' },
    { id: '_23_window_handling___', title: '23. Windows', icon: 'fa-window-restore' },
    { id: '_24_file_upload_download___', title: '24. File Up/Down', icon: 'fa-upload' },
    { id: '_25_screenshots___', title: '25. Screenshots', icon: 'fa-camera' },
    { id: '_26_common_selenium_exceptions___', title: '26. Exceptions', icon: 'fa-bug' },
    { id: '_27_page_object_model___', title: '27. POM Pattern', icon: 'fa-sitemap' },
    { id: '_28_testng___', title: '28. TestNG', icon: 'fa-vial' },
    { id: '_29_maven_and_project_structure___', title: '29. Maven', icon: 'fa-box' },
    { id: '_30_reports___', title: '30. Reports', icon: 'fa-chart-line' },
    { id: '_31_extra___', title: '31. Resources', icon: 'fa-star' },
    { id: '_32_connect_with_local_host', title: '32. Local Testing', icon: 'fa-server' }
];

function populateSidebar() {
    const topicList = document.getElementById('topic-list');
    if (!topicList) return;
    
    const sections = [
        { label: '📌 Getting Started', topics: [0, 1, 2] },
        { label: '⚙️ Setup & Commands', topics: [3, 4, 5, 6] },
        { label: '🔍 Locators & Selection', topics: [7, 8] },
        { label: '📝 HTML Controls', topics: [9, 10, 11] },
        { label: '⚡ Advanced Interactions', topics: [12, 13, 14, 15, 16, 17, 18, 19, 20] },
        { label: '🛠️ Utilities & Tools', topics: [21, 22, 23, 24, 25] },
        { label: '🧪 Framework & Design', topics: [26, 27, 28, 29] },
        { label: '🏁 Resources', topics: [30, 31] }
    ];

    sections.forEach(section => {
        const sectionDiv = document.createElement('div');
        sectionDiv.className = 'sidebar-section';
        
        const label = document.createElement('div');
        label.className = 'sidebar-section-label';
        label.textContent = section.label;
        sectionDiv.appendChild(label);
        
        const ul = document.createElement('ul');
        section.topics.forEach(index => {
            const topic = topics[index];
            const li = document.createElement('li');
            const a = document.createElement('a');
            a.href = '../content/' + topic.id + '.html';
            
            // Check if this is the current page
            const isActive = window.location.pathname.includes(topic.id);
            a.className = 'topic-link' + (isActive ? ' active' : '');
            a.innerHTML = '<i class="fas ' + topic.icon + '"></i> ' + topic.title;
            li.appendChild(a);
            ul.appendChild(li);
        });
        sectionDiv.appendChild(ul);
        topicList.appendChild(sectionDiv);
    });
}

function goHome() {
    window.location.href = '../index.html';
}

// Initialize sidebar when DOM is ready
if (document.readyState === 'loading') {
    document.addEventListener('DOMContentLoaded', populateSidebar);
} else {
    populateSidebar();
}
