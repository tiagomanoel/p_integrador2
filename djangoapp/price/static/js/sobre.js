// Remove the loading overlay after the page loads
window.addEventListener('load', function() {
    document.querySelector('.loading-overlay').style.display = 'none';
    const container = document.querySelector('.container');
    container.style.display = 'block';
    // Adds the 'show' class to trigger the fade-in animation
    setTimeout(() => {
        container.classList.add('show');
    }, 50); // Brief delay to ensure the CSS is applied
});
