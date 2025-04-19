// scroll.js
document.addEventListener('DOMContentLoaded', () => {
    console.log("Scroll event script loaded!");

    // Create a "Back to Top" button
    const backToTopButton = document.createElement('button');
    backToTopButton.textContent = '↑';
    backToTopButton.style.position = 'fixed';
    backToTopButton.style.bottom = '20px';
    backToTopButton.style.right = '20px';
    backToTopButton.style.display = 'none';
    backToTopButton.style.padding = '12px 24px';
    backToTopButton.style.backgroundColor = 'rgba(44, 62, 80, 0.7)'; // Semi-transparent #2c3e50
    backToTopButton.style.color = '#fff';
    backToTopButton.style.border = 'none';
    backToTopButton.style.borderRadius = '25px'; // More rounded corners
    backToTopButton.style.cursor = 'pointer';
    backToTopButton.style.fontSize = '14px';
    backToTopButton.style.fontWeight = '600';
    backToTopButton.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.2)'; // Subtle shadow
    backToTopButton.style.transition = 'all 0.3s ease'; // Smooth transition for hover effects
    backToTopButton.style.zIndex = '1000'; // Ensure it's above other elements
    document.body.appendChild(backToTopButton);

    // Add hover effects
    backToTopButton.addEventListener('mouseover', () => {
        backToTopButton.style.backgroundColor = 'rgba(44, 62, 80, 1)'; // Fully opaque on hover
        backToTopButton.style.boxShadow = '0 6px 16px rgba(0, 0, 0, 0.3)'; // Enhanced shadow on hover
    });

    backToTopButton.addEventListener('mouseout', () => {
        backToTopButton.style.backgroundColor = 'rgba(44, 62, 80, 0.8)'; // Semi-transparent again
        backToTopButton.style.boxShadow = '0 4px 12px rgba(0, 0, 0, 0.2)'; // Revert shadow
    });

    // Add scroll event listener to show/hide the button
    window.addEventListener('scroll', () => {
        console.log(`Scroll Y position: ${window.scrollY}`); // Debugging
        if (window.scrollY > 300) {
            console.log("Showing Back to Top button!"); // Debugging
            backToTopButton.style.display = 'block';
        } else {
            console.log("Hiding Back to Top button!"); // Debugging
            backToTopButton.style.display = 'none';
        }
    });

    // Add click event listener to scroll to the top
    backToTopButton.addEventListener('click', () => {
        console.log("Scrolled to the top!"); // Debugging
        window.scrollTo({ top: 0, behavior: 'smooth' }); // Smooth scroll to the top
    });
});