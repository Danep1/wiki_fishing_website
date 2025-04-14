document.addEventListener('DOMContentLoaded', function() {
    const closeModalButton = document.querySelector('.close-modal');
    const modalOverlay = document.querySelector('.modal-overlay');


    if (closeModalButton && modalOverlay) {
        closeModalButton.addEventListener('click', function() {
            window.history.back();
        });
    }

    // Закрытие по ESC
    document.addEventListener('keydown', function(e) {
        if (e.key === 'Escape') {
            window.history.back();
        }
    });
});
