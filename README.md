# Deligo - Online Food Delivery Platform

# Deligo - Django-Based Online Food Delivery Platform

## Project Overview

**Deligo** is a Django-based web application that facilitates food ordering between customers and restaurant managers. Built as part of a university coursework project, the application supports user authentication, dynamic menu displays, cart functionality, order placement, and manager order tracking — all integrated with a relational SQLite database.

Deligo replaces static HTML/JS with a full server-side architecture using Django, forms, models, AJAX, and database connectivity.

---

## Application Domain

- **Domain**: Online Food Ordering & Delivery
- **Target Users**: 
  - **Customers**: Browse restaurants, add food to cart, checkout.
  - **Restaurant Managers**: Manage orders, update order status.
- **Use Case**: Simulates a real-world food delivery service such as UberEats or Deliveroo for learning full-stack development using Django.

---

## Features Implemented

- User registration & login with role-based access (`Customer`, `Manager`)
- Browse restaurants and dynamically loaded menu items
- Quantity controls with **AJAX-based Add to Cart**
- Global cart support across restaurants
- Full cart management (update quantity, remove items)
- Order placement & automatic total calculation
- Manager dashboard for viewing and updating order status
- AJAX checkout handling with redirection
- Profile editing with form validation

---

## Project Structure


### CSS Files
- **stylesheets/style.css**: Global styles used across all pages.
- **stylesheets/login.css**: Styles specific to the login page.
- **stylesheets/home.css**: Styles specific to the home page.
- **stylesheets/restaurants.css**: Styles specific to the restaurants page.
- **stylesheets/menu.css**: Styles specific to the menu page.
- **stylesheets/cart.css**: Styles specific to the cart page.
- **stylesheets/contact.css**: Styles specific to the contact page.
- **stylesheets/register.css**: Styles specific to the registration page.
- **stylesheets/menubar.css**: Styles for the dynamic menu bar (hamburger menu).

### JavaScript Files
- **scripts/menu.js**: Handles the dynamic menu bar functionality, including toggling the menu and animating the hamburger icon.
- **scripts/validation.js**: Implements form validation for the login, registration, and contact forms.
- **scripts/storage.js**: Manages local storage for storing user data and form responses.
- **scripts/events.js**: Handles event listeners for tooltips, form submissions, and other interactions.
- **scripts/right-click.js**: Disables right-clicking on images and displays an alert.
- **scripts/scroll.js**: Implements the "Back to Top" button that appears when scrolling down.

### Images Folder
- **images/**: Contains all images used in the project, such as the logo (`logo.jpg`), dish images (`dish1.jpg`, `dish2.jpg`...), and restaurant images (`restaurant1.jpg`, `restaurant2.jpg`,....).

By default, this will start the server on port 8000. You can access your HTML file by visiting http://localhost:8000 in your browser.

If you want to specify a different port, you can do so by providing the port number:

bash
Copy code
python -m http.server 8080
This will run the server on http://localhost:8080.


## Future Enhancements
In the future, Deligo will be enhanced with:
- JavaScript for dynamic functionality (e.g., updating the cart in real-time).
- A database to store user information, restaurant menus, and order details.
- APIs to fetch real-time data, such as restaurant menus and user reviews.
- A responsive design for optimization across all devices.

## How to Contribute
1. Fork the repository.
2. Create a new branch for your feature or bug fix.
3. Commit your changes and push them to your branch.
4. Submit a pull request with a detailed description of your changes.


## Contact
For any questions or feedback, please contact:
- **Email**: [saikoushikjuttu@gmail.com]
- **GitHub**: [https://github.com/Koushikpatel8]

cd "deligo_project"
1. venv\Scripts\activate
2. pip install -r requirements.txt
python manage.py makemigrations
python manage.py migrate



python manage.py runserver
