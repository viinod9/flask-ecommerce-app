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

## 🛠️ Project Structure

```
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
```

---

## 🛠️ Installation

1️⃣ Clone the repository

```bash
git clone https://github.com/<viinod9>/flask-ecommerce-app.git
cd flask-ecommerce-app
```

2️⃣ Create and activate virtual environment

```bash
python3 -m venv flask_venv
source flask_venv/bin/activate
```

3️⃣ Install dependencies

```bash
pip install -r requirements.txt
```

---

## ✅ Database Initialization

Open Python shell:

```bash
python
```

Run the following commands to create database tables:

```python
from app import create_app
from app.extensions import db

app = create_app()
app.app_context().push()
db.create_all()
exit()
```

(Optional) Add sample products:

```python
from app import create_app
from app.extensions import db
from app.models import Product

app = create_app()
app.app_context().push()

product1 = Product(name="Laptop", price=999.99)
product2 = Product(name="Smartphone", price=499.99)

db.session.add_all([product1, product2])
db.session.commit()
exit()
```

---

## ▶️ Running the Application

```bash
python run.py
```

Visit in browser:

```
http://127.0.0.1:5000/auth/signup
```

Flow:  
Signup → Login → Products → Add to Cart → View Cart

---

## 🔧 Deactivate Virtual Environment

```bash
deactivate
```

---

## 📦 Dependencies

All dependencies are listed in `requirements.txt`.  
To regenerate (if needed):

```bash
pip freeze > requirements.txt
```

---

## 📚 Notes

- Uses SQLite for simplicity  
- Passwords are hashed using `pbkdf2:sha256`  
- Modular structure using Flask Blueprints

---

## 📧 Contact

Created by [Vinod Kumar]  
GitHub: [https://github.com/<viinod9>](https://github.com/<viinod9>)
