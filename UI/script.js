const aboutBtn = document.getElementById("about-btn");
const modalClose = document.getElementById("close-btn");

aboutBtn.addEventListener('click', () => openModal());
modalClose.addEventListener('click', () => closeModal());

function openModal() {
    document.getElementById('aboutModal').classList.add('active');
}

function closeModal() {
    document.getElementById('aboutModal').classList.remove('active');
}

// Close modal with Escape key
document.addEventListener('keydown', function(event) {
    if (event.key === 'Escape') {
        closeModal();
    }
});