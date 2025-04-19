# sample_data.py

from food_delivery.models import User, Restaurant, MenuCategory, MenuItem

# Create a restaurant manager
manager = User.objects.create_user(
    username='manager1',
    email='manager@example.com',
    password='test1234',
    type=User.Types.RESTAURANT_MANAGER
)

# Create a restaurant and link it to the manager
restaurant = Restaurant.objects.create(
    name='Deligo Diner',
    description='A taste of home.',
    address='123 Food St, Flavor Town',
    contact_number='1234567890',
    opening_hours='10am - 10pm',
    manager=manager
)

# Add a menu category
category = MenuCategory.objects.create(
    restaurant=restaurant,
    name='Main Course',
    order=1
)

# Add menu items under the category
MenuItem.objects.create(
    category=category,
    name='Grilled Chicken',
    description='Served with fries and salad',
    price=12.99,
    is_available=True,
    preparation_time=20
)

MenuItem.objects.create(
    category=category,
    name='Veggie Burger',
    description='Delicious plant-based burger with fresh toppings',
    price=8.99,
    is_available=True,
    preparation_time=15
)

print("✅ Sample data created successfully.")
