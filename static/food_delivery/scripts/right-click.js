// right-click.js
document.addEventListener('DOMContentLoaded', () => {
    console.log("Right-click event script loaded!");

    // Select all images on the page
    const images = document.querySelectorAll('img');
    console.log(images); // Debugging: Check if images are selected

    // Add contextmenu (right-click) event listener to each image
    images.forEach(image => {
        image.addEventListener('contextmenu', (e) => {
            console.log("Right-click detected!"); // Debugging
            e.preventDefault(); // Prevent the default right-click menu
            alert('Right-click is disabled on images.'); // Notify the user
        });
    });
});