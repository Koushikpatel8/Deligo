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
            // If the form is valid, allow it to submit and redirect
            console.log("Form is valid. Redirecting to home.html...");
            window.location.href = "home.html"; // Redirect to home.html
        }
    });
}