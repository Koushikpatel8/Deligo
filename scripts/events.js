// scripts/events.js
const submitButton = document.getElementById('submit-button');
const tooltip = document.getElementById('tooltip');

submitButton.addEventListener('click', () => {
    alert('Form submitted successfully!');
});

submitButton.addEventListener('mouseover', () => {
    tooltip.style.display = 'block';
});

submitButton.addEventListener('mouseout', () => {
    tooltip.style.display = 'none';
});