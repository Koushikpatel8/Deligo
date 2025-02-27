document.addEventListener('DOMContentLoaded', () => {
    console.log("Events script loaded!");

    // Select the email input and hint elements
    const emailInput = document.getElementById('email');
    const emailHint = document.getElementById('email-hint');

    // Check if the email input and hint exist
    if (emailInput && emailHint) {
        console.log("Email input and hint found!");

        // Add a focus event listener to the email input
        emailInput.addEventListener('focus', () => {
            console.log("Email input focused!");
            emailHint.textContent = "Please enter a valid email address (e.g., user@example.com).";
            emailHint.style.display = 'block'; // Show the hint
        });

        // Add a blur event listener to the email input
        emailInput.addEventListener('blur', () => {
            console.log("Email input blurred!");
            emailHint.style.display = 'none'; // Hide the hint
        });
    } else {
        console.error("Email input or hint not found!");
    }
});