Inventory Management API
An API for managing inventory items, user authentication, and inventory tracking. Built with Django, Django REST Framework (DRF), and deployed on Heroku.

# inventory-api
This is my final capstone project, a backend inventory management API 


Features
User Authentication: Secure authentication using JSON Web Tokens (JWT).
Inventory Management: CRUD operations for inventory items.
Pagination & Filtering: Supports pagination, filtering, and ordering of inventory data.
Report Generation
Heroku Deployment: Ready for cloud hosting.

Technologies Used
Backend Framework: Django, Django REST Framework
Database: SQLite (development), PostgreSQL (production)
Deployment: Heroku
# Inventory Management Project

## Setup Instructions
1. Clone the repository:
   ```bash
   git clone (https://github.com/MSZAKARIA1/inventory-api.git)

2.Navigate to the project directory: 
cd <inventory-api>

3.Create and activate a virtual environment:
virtualenv myvenv
source venv/bin/activate  # For Windows: venv\Scripts\activate

4.Install dependencies:
pip install -r requirements.txt

5. Run migrations:
python manage.py makemigrations
python manage.py migrate

6. Start the development server:
python manage.py runserver

****************************Endpoints ************************
#Here are the various endpoints

*********************Authentication*****************************
https://inventory-api-da1c010c0f13.herokuapp.com/api/token/
https://inventory-api-da1c010c0f13.herokuapp.com/api/token/refresh

  *********************Inventory Management ***********************
 "users": "https://inventory-api-da1c010c0f13.herokuapp.com/api/users/",
    "categories": "https://inventory-api-da1c010c0f13.herokuapp.com/api/categories/",
    "suppliers": "https://inventory-api-da1c010c0f13.herokuapp.com/api/suppliers/",
    "products": "https://inventory-api-da1c010c0f13.herokuapp.com/api/products/",
    "orders": "https://inventory-api-da1c010c0f13.herokuapp.com/api/orders/",
    "inventory-history": "https://inventory-api-da1c010c0f13.herokuapp.com/api/inventory-history/",
    "reports": "https://inventory-api-da1c010c0f13.herokuapp.com/api/reports/"

********************Contributing**********************
Fork the repository.
Create a new branch for your feature or bug fix:
bash
Copy code
git checkout -b feature-name
Commit your changes:
bash
Copy code
git commit -m "Add feature-name"
Push to your branch:
bash
Copy code
git push origin feature-name
Open a pull request.

**********************Contact**********************
For inquiries or support, email: zakariamahamasaani@gmail.com
