// Waits for the page to fully load
document.addEventListener("DOMContentLoaded", () => {
    const fadeElements = document.querySelectorAll('.fade-in');

    fadeElements.forEach((el, index) => {
        // Adds a delay between the animations of each card
        el.style.animationDelay = `${index * 0.3}s`;
        el.classList.add('show'); // Adds the class to trigger the animation
    });
});


