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
- Quantity controls with AJAX-based Add to Cart  
- Global cart support across restaurants  
- Full cart management (update quantity, remove items)  
- Order placement & automatic total calculation  
- Manager dashboard for viewing and updating order status  
- AJAX checkout handling with redirection  
- Profile editing with form validation  

---

## Setup Instructions

### Prerequisites

- Python 3.9+ (preferably 3.10+)  
- pip (Python package manager)  
- Virtual environment  

### Step-by-Step Installation

```bash
# 1. Clone the project
git clone https://github.com/Koushikpatel8/Deligo.git
cd deligo_project

# 2. Create and activate virtual environment
python -m venv venv
venv\Scripts\activate       # On Windows
# or
source venv/bin/activate    # On macOS/Linux

# 3. Install dependencies
pip install -r requirements.txt

# 4. Apply database migrations
python manage.py makemigrations
python manage.py migrate

# 5. Create superuser (optional, for admin access)
python manage.py createsuperuser

# 6. Start the development server
python manage.py runserver
```

This will run the server on http://localhost:8000.  
Visit: http://127.0.0.1:8000/ to use the app.

---

## Sample Test Users

**Customer**  
- Username: customer1  
- Password: customer1  

**Manager**  
- Username: manager1  
- Password: manager1  

You can also register new accounts via the web interface by clicking on Register as a new customer.

---

## Database Models

- **User** (Custom model with roles)  
- **CustomerProfile** (linked to User)  
- **Restaurant** (with manager)  
- **MenuCategory** and **MenuItem**  
- **Order** and **OrderItem**  

All CRUD operations are powered by Django ORM and validated via Django Forms.

---

## Technologies Used

- Django 4.2  
- SQLite3  
- HTML + CSS (Bootstrap-like design)  
- JavaScript & AJAX  
- Django Templates + Static Files  
- VS Code (Development environment)  

---

## Features You Can Test

- Register as a new customer  
- Add multiple dishes with quantity  
- Navigate and update cart dynamically  
- Proceed to checkout via AJAX  
- As a manager: View dashboard and change order status  

---

## Additional Notes

- Use the Django admin panel (`/admin`) to quickly add restaurants, managers, and menu items.  
- All JavaScript files are cleanly separated for AJAX and menu functionality.  
- Quantity updates and add-to-cart work without page reloads.  

---

## How to Contribute

1. Fork the repository.  
2. Create a new branch for your feature or bug fix.  
3. Commit your changes and push them to your branch.  
4. Submit a pull request with a detailed description of your changes.  

---

## Contact

For any questions or feedback, please contact:

- **Email**: saikoushikjuttu@gmail.com  
- **GitHub**: [https://github.com/Koushikpatel8](https://github.com/Koushikpatel8)

For any issues, feel free to reach out via email or GitHub. Thank you!
