// scripts/events.js

// Select the submit button and tooltip elements
const submitButton = document.getElementById('submit-button');
const tooltip = document.getElementById('tooltip');

// Add a click event listener to the submit button
submitButton.addEventListener('click', () => {
    alert('Form submitted successfully!'); // Show an alert when the form is submitted
});

// Add a mouseover event listener to the submit button
submitButton.addEventListener('mouseover', () => {
    tooltip.style.display = 'block'; // Show the tooltip when the mouse is over the button
});

// Add a mouseout event listener to the submit button
submitButton.addEventListener('mouseout', () => {
    tooltip.style.display = 'none'; // Hide the tooltip when the mouse leaves the button
});