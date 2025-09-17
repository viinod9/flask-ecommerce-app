# Flask E-Commerce App

A modular Flask-based e-commerce web application that supports user signup, login, product listing, adding products to cart, and cart management.

---

## 🚀 Features

- User Signup and Login (with password hashing)
- Product Listing
- Add Products to Cart
- View Cart
- Modular Code Structure with Blueprints
- SQLite Database Backend

---

## ⚙️ Project Structure


Flask/
├── flask_venv/                # Virtual environment
├── run.py                     # Entry point to run the app
├── config.py                  # App configuration (DB, secret key)

├── app/
│   ├── __init__.py            # App factory
│   ├── models.py              # Database models (User, Product, Cart)
│   ├── extensions.py          # Flask extensions (db, login manager)
│   │
│   ├── auth/                  # Authentication module (signup, login)
│   │   └── routes.py
│   │
│   ├── shop/                  # Shop module (products, cart)
│   │   └── routes.py
│   │
│   ├── templates/             # Jinja2 templates
│   │   ├── base.html
│   │   ├── auth/
│   │   │   ├── login.html
│   │   │   └── signup.html
│   │   └── shop/
│   │       ├── products.html
│   │       └── cart.html
│   │
│   └── static/                # Static files (CSS, JS, images)

├── ecommerce.db               # SQLite database (auto-generated)
├── requirements.txt           # Project dependencies
└── .gitignore










