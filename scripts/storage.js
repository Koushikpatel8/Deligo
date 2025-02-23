// Wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', () => {
    console.log("Storage script loaded!");

    // Function to validate the registration form
    function validateRegistrationForm(fullName, email, password, confirmPassword) {
        let isValid = true;

        // Full Name validation
        if (fullName.trim() === '') {
            console.log("Full Name is required."); // Debugging
            isValid = false;
        }

        // Email validation
        const emailRegex = /^[^\s@]+@[^\s@]+\.[^\s@]+$/;
        if (email.trim() === '') {
            console.log("Email is required."); // Debugging
            isValid = false;
        } else if (!emailRegex.test(email)) {
            console.log("Please enter a valid email address."); // Debugging
            isValid = false;
        }

        // Password validation
        if (password.trim() === '') {
            console.log("Password is required."); // Debugging
            isValid = false;
        } else if (password.length < 8) {
            console.log("Password must be at least 8 characters long."); // Debugging
            isValid = false;
        }

        // Confirm Password validation
        if (confirmPassword.trim() === '') {
            console.log("Confirm Password is required."); // Debugging
            isValid = false;
        } else if (confirmPassword !== password) {
            console.log("Passwords do not match."); // Debugging
            isValid = false;
        }

        return isValid;
    }

    // Function to save form data to localStorage
    function saveFormData(formId, storageKey, validate = false) {
        const form = document.getElementById(formId);
        if (form) {
            console.log(`Form with ID ${formId} found!`); // Debugging
            form.addEventListener('submit', (e) => {
                console.log('Form submitted!'); // Debugging
                e.preventDefault(); // Prevent the form from submitting

                // Capture form data
                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries()); // Convert to an object
                console.log('Form data captured:', data); // Debugging

                // Validate the form data (only for registration form)
                if (validate) {
                    const isValid = validateRegistrationForm(
                        data['full-name'], // Full Name
                        data.email,        // Email
                        data.password,     // Password
                        data['confirm-password'] // Confirm Password
                    );

                    if (!isValid) {
                        console.log('Form validation failed!'); // Debugging
                        alert('Please fill in all fields correctly.'); // Notify the user
                        return; // Stop further execution
                    }
                }

                // Get existing data or initialize an empty array
                const responses = JSON.parse(localStorage.getItem(storageKey)) || [];
                responses.push(data); // Add new data to the array

                // Save back to localStorage
                localStorage.setItem(storageKey, JSON.stringify(responses));
                console.log('Data saved to localStorage:', responses); // Debugging

                // Clear the form
                form.reset();
                console.log('Form reset!'); // Debugging

                // Notify the user
                alert('Data saved successfully!'); // Debugging
                console.log('Alert shown!'); // Debugging
            });
        } else {
            console.error(`Form with ID ${formId} not found!`);
        }
    }

    // Function to display stored data in a table
    function displayData(storageKey, tableId) {
        const tableBody = document.getElementById(tableId).getElementsByTagName('tbody')[0];
        if (tableBody) {
            const responses = JSON.parse(localStorage.getItem(storageKey)) || []; // Get stored data or initialize an empty array
            console.log('Data retrieved from localStorage:', responses); // Debugging
            tableBody.innerHTML = ''; // Clear the table before displaying new data

            // Populate the table with stored data
            responses.forEach(response => {
                const row = tableBody.insertRow(); // Insert a new row
                for (const key in response) {
                    row.insertCell().textContent = response[key]; // Insert cells with data
                }
            });
        } else {
            console.error(`Table body with ID ${tableId} not found!`);
        }
    }

    // Save and display data for the login form
    saveFormData('login-form', 'logins');

    // Add event listener for "View Logins" button
    const viewLoginsButton = document.getElementById('view-logins');
    if (viewLoginsButton) {
        viewLoginsButton.addEventListener('click', () => {
            console.log('View Logins button clicked!'); // Debugging
            displayData('logins', 'logins-table');
        });
    } else {
        console.error('View Logins button not found!');
    }

    // Save and display data for the registration form
    saveFormData('registration-form', 'registrations', true); // Enable validation for registration form

    // Add event listener for "View Registrations" button
    const viewRegistrationsButton = document.getElementById('view-registrations');
    if (viewRegistrationsButton) {
        viewRegistrationsButton.addEventListener('click', () => {
            console.log('View Registrations button clicked!'); // Debugging
            displayData('registrations', 'registrations-table');
        });
    } else {
        console.error('View Registrations button not found!');
    }
});