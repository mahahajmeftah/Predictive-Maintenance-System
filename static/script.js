document.addEventListener('DOMContentLoaded', function () {
    const sidebar = document.getElementById('sidebar');
    const content = document.getElementById('content');
    const closeBtn = document.getElementById('close-btn');
    const openBtn = document.getElementById('open-btn');

    closeBtn.addEventListener('click', function () {
        sidebar.classList.add('hidden');
        content.classList.add('expanded');
        openBtn.classList.add('visible');
    });

    openBtn.addEventListener('click', function () {
        sidebar.classList.remove('hidden');
        content.classList.remove('expanded');
        openBtn.classList.remove('visible');
    });
});