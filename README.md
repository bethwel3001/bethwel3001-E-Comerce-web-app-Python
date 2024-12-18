## Py_E-Comerce-web-app
# E-Commerce Web App
This is a simple **E-Commerce Web Application** built with **Python Flask**, **HTML**, **CSS**, and connected to a **MySQL** database. The app allows users to browse products, add them to a shopping cart, and make orders. Admins can manage product listings and view customer orders.

## Features

- **User Features:**
  - Browse and search products.
  - View detailed product information.
  - Add products to the shopping cart.
  - Checkout and place orders.
  - User registration and login.

- **Admin Features:**
  - Admin dashboard to manage products.
  - View all orders placed by customers.
  - Manage product inventory (add, update, delete products).

## Technologies

- **Backend**: Python, Flask
- **Frontend**: HTML, CSS (Bootstrap for responsive design)
- **Database**: MySQL
- **ORM**: SQLAlchemy (for database interaction)
- **Authentication**: Flask-Login
- **Form Handling**: Flask-WTF

## Installation
- Flask==2.1.0
- Flask-SQLAlchemy==2.5.1
- Flask-Login==0.5.0
- Flask-WTF==1.0.0
- mysql-connector-python==8.0.27

### Prerequisites

- Python 3.x
- MySQL Server installed on your machine.
  
## Dependencies
This project uses the following Python dependencies:

- *Flask:* A lightweight WSGI web application framework. Flask Documentation
- *Flask-SQLAlchemy:* SQLAlchemy integration for Flask. Flask-SQLAlchemy Documentation
- *Flask-Login:* User session management for Flask. Flask-Login Documentation
- *Flask-WTF:* Forms for Flask with CSRF protection. Flask-WTF Documentation
- *MySQL:* MySQL database server. MySQL Documentation
- *Bootstrap:* Frontend CSS framework used for layout and styling. Bootstrap Documentation

## Contributing
We welcome contributions from the community! To contribute:

1. Fork the repository.
2. Create a new branch (git checkout -b feature-name).
3. Make your changes and commit them (git commit -m 'Add new feature').
4. Push to the branch (git push origin feature-name).
5. Open a pull request.
Please ensure your code adheres to the existing style and includes appropriate tests and documentation.

## License
This project is licensed under the MIT License - see the LICENSE file for details.

## Acknowledgements
**Flask:** For providing a lightweight framework to build web apps in Python.
**Bootstrap:** For the responsive front-end framework.
**MySQL:** For the relational database backend.
### 1. Clone the repository

```bash
git clone https://github.com/bethwel3001/e-commerce-web-app.git
cd e-commerce-web-app

# Create a virtual environment (optional)
python3 -m venv venv
source venv/bin/activate  # On Windows: venv\Scripts\activate
# Install dependencies
pip install -r requirements.txt
# Set up the database
Create a MySQL database and update the database configuration in app.py
CREATE DATABASE ecommerce_db;
SQLALCHEMY_DATABASE_URI = 'mysql://username:password@localhost/ecommerce_db'

# Run the application
python app.py
Access the application in your web browser at http://localhost:5000
## Usage

To run the application, execute the following command in your terminal:
```bash
python app.py
flask run
```
# Dev.Bethwel Kiplangat