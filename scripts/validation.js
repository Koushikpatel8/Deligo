// Wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', () => {
    console.log("Validation script loaded!");

    // Login Form Validation
    const loginForm = document.getElementById('login-form');
    if (loginForm) {
        const loginEmailInput = document.getElementById('email');
        const loginPasswordInput = document.getElementById('password');
        
        const loginEmailError = document.getElementById('email-error');
        const loginPasswordError = document.getElementById('password-error');

        loginForm.addEventListener('submit', (e) => {
            console.log("Login form submitted!");
            let isValid = true;

            // Clear previous error messages and styles
            loginEmailError.textContent = '';
            loginEmailError.classList.remove('show');
            loginEmailInput.classList.remove('error-field');

            loginPasswordError.textContent = '';
            loginPasswordError.classList.remove('show');
            loginPasswordInput.classList.remove('error-field');

            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (loginEmailInput.value.trim() === '') {
                loginEmailError.textContent = 'Email is required.';
                loginEmailError.classList.add('show');
                loginEmailInput.classList.add('error-field');
                isValid = false;
            } else if (!emailRegex.test(loginEmailInput.value)) {
                loginEmailError.textContent = 'Please enter a valid email address.';
                loginEmailError.classList.add('show');
                loginEmailInput.classList.add('error-field');
                isValid = false;
            }

            // Password validation
            if (loginPasswordInput.value.trim() === '') {
                loginPasswordError.textContent = 'Password is required.';
                loginPasswordError.classList.add('show');
                loginPasswordInput.classList.add('error-field');
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                e.preventDefault(); // Stop form submission
            } else {
                // If the form is valid, allow it to submit
                console.log("Form is valid. Redirecting to home.html...");
                window.location.href = "home.html"; // Redirect to home.html
            }
        });
    }

    // Contact Form Validation
    const feedbackForm = document.getElementById('feedback-form');
    if (feedbackForm) {
        const nameInput = document.getElementById('name');
        const emailInput = document.getElementById('email');
        const messageInput = document.getElementById('message');
        
        const nameError = document.getElementById('name-error');
        const emailError = document.getElementById('email-error');
        const messageError = document.getElementById('message-error');

        feedbackForm.addEventListener('submit', (e) => {
            console.log("Contact form submitted!");
            let isValid = true;

            // Clear previous error messages and styles
            nameError.textContent = '';
            nameError.classList.remove('show');
            nameInput.classList.remove('error-field');

            emailError.textContent = '';
            emailError.classList.remove('show');
            emailInput.classList.remove('error-field');

            messageError.textContent = '';
            messageError.classList.remove('show');
            messageInput.classList.remove('error-field');

            // Name validation
            if (nameInput.value.trim() === '') {
                nameError.textContent = 'Name is required.';
                nameError.classList.add('show');
                nameInput.classList.add('error-field');
                isValid = false;
            }

            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (emailInput.value.trim() === '') {
                emailError.textContent = 'Email is required.';
                emailError.classList.add('show');
                emailInput.classList.add('error-field');
                isValid = false;
            } else if (!emailRegex.test(emailInput.value)) {
                emailError.textContent = 'Please enter a valid email address.';
                emailError.classList.add('show');
                emailInput.classList.add('error-field');
                isValid = false;
            }

            // Message validation
            if (messageInput.value.trim() === '') {
                messageError.textContent = 'Message is required.';
                messageError.classList.add('show');
                messageInput.classList.add('error-field');
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                e.preventDefault(); // Stop form submission
            }
        });
    }

    // Registration Form Validation
    const registrationForm = document.getElementById('registration-form');
    if (registrationForm) {
        console.log("Registration form found!"); // Debugging

        const fullNameInput = document.getElementById('full-name');
        const emailInput = document.getElementById('email');
        const passwordInput = document.getElementById('password');
        const confirmPasswordInput = document.getElementById('confirm-password');
        
        const fullNameError = document.getElementById('full-name-error');
        const emailError = document.getElementById('email-error');
        const passwordError = document.getElementById('password-error');
        const confirmPasswordError = document.getElementById('confirm-password-error');

        registrationForm.addEventListener('submit', (e) => {
            console.log("Registration form submitted!"); // Debugging
            let isValid = true;

            // Clear previous error messages and styles
            fullNameError.textContent = '';
            fullNameError.classList.remove('show');
            fullNameInput.classList.remove('error-field');

            emailError.textContent = '';
            emailError.classList.remove('show');
            emailInput.classList.remove('error-field');

            passwordError.textContent = '';
            passwordError.classList.remove('show');
            passwordInput.classList.remove('error-field');

            confirmPasswordError.textContent = '';
            confirmPasswordError.classList.remove('show');
            confirmPasswordInput.classList.remove('error-field');

            // Full Name validation
            if (fullNameInput.value.trim() === '') {
                console.log("Full Name is required."); // Debugging
                fullNameError.textContent = 'Full Name is required.';
                fullNameError.classList.add('show');
                fullNameInput.classList.add('error-field');
                isValid = false;
            }

            // Email validation
            const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
            if (emailInput.value.trim() === '') {
                console.log("Email is required."); // Debugging
                emailError.textContent = 'Email is required.';
                emailError.classList.add('show');
                emailInput.classList.add('error-field');
                isValid = false;
            } else if (!emailRegex.test(emailInput.value)) {
                console.log("Please enter a valid email address."); // Debugging
                emailError.textContent = 'Please enter a valid email address.';
                emailError.classList.add('show');
                emailInput.classList.add('error-field');
                isValid = false;
            }

            // Password validation
            if (passwordInput.value.trim() === '') {
                console.log("Password is required."); // Debugging
                passwordError.textContent = 'Password is required.';
                passwordError.classList.add('show');
                passwordInput.classList.add('error-field');
                isValid = false;
            } else if (passwordInput.value.length < 8) {
                console.log("Password must be at least 8 characters long."); // Debugging
                passwordError.textContent = 'Password must be at least 8 characters long.';
                passwordError.classList.add('show');
                passwordInput.classList.add('error-field');
                isValid = false;
            }

            // Confirm Password validation
            if (confirmPasswordInput.value.trim() === '') {
                console.log("Confirm Password is required."); // Debugging
                confirmPasswordError.textContent = 'Confirm Password is required.';
                confirmPasswordError.classList.add('show');
                confirmPasswordInput.classList.add('error-field');
                isValid = false;
            } else if (confirmPasswordInput.value !== passwordInput.value) {
                console.log("Passwords do not match."); // Debugging
                confirmPasswordError.textContent = 'Passwords do not match.';
                confirmPasswordError.classList.add('show');
                confirmPasswordInput.classList.add('error-field');
                isValid = false;
            }

            // Prevent form submission if validation fails
            if (!isValid) {
                console.log("Form is invalid. Preventing submission."); // Debugging
                e.preventDefault(); // Stop form submission
            }
        });
    } else {
        console.log("Registration form not found!"); // Debugging
    }
});