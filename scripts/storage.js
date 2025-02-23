// Wait for the DOM to load before running the script
document.addEventListener('DOMContentLoaded', () => {
    console.log("Storage script loaded!");

    // Function to save form data to localStorage
    function saveFormData(formId, storageKey) {
        const form = document.getElementById(formId);
        if (form) {
            console.log(`Form with ID ${formId} found!`); // Debugging
            form.addEventListener('submit', (e) => {
                console.log('Form submitted!'); // Debugging

                // Capture form data
                const formData = new FormData(form);
                const data = Object.fromEntries(formData.entries()); // Convert to an object
                console.log('Form data captured:', data); // Debugging

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
                alert('Data saved successfully!');
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
                    const cell = row.insertCell();
                    cell.textContent = response[key]; // Insert cells with data
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
});