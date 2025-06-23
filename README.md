# 🖨️ WePrint - Django E-commerce Printing Platform

**WePrint** is an online printing shop built with Django. It allows customers to browse print products (like business cards, flyers, posters), view product details, and place orders seamlessly.

---

## 🚀 Features

- 🛍️ Product listing with images and prices  
- 🔍 Product detail page with order form  
- 🖼️ Media support (uploads and displays product images)  
- 🛠️ Admin panel to manage products and orders  
- 💽 SQLite database (easy to set up)  
- 🌐 Responsive frontend templates (customizable)

---

## 📸 Screenshots

### 🔐 Admin Panel
![Admin Panel](screenshots/admin-panel.png)

### 🏠 Homepage
![Homepage](screenshots/homepage.png)

### 📦 Product Detail Page
![Product Detail](screenshots/product-detail.png)

---

## 🧰 Tech Stack

- Python 3.12  
- Django 5.2.3  
- HTML / CSS (with Bootstrap-ready layout)  
- SQLite3  
- Pillow for image handling

---

## ⚙️ Installation & Setup

```bash
# Clone the repository
git clone https://github.com/ugbedethomas/weprint-django.git
cd weprint-django

# Create virtual environment
python -m venv venv
source venv/Scripts/activate  # On Windows
# or
source venv/bin/activate  # On macOS/Linux

# Install dependencies
pip install -r requirements.txt

# Run migrations
python manage.py migrate

# Create superuser
python manage.py createsuperuser

# Start server
python manage.py runserver

🧠 Default site: http://127.0.0.1:8000

🙋🏽‍♂️ Author
Augustine Ugbede Thomas
🎯 GitHub
📍 Nigeria 🇳🇬 | Tech founder @ Stinet Digital

📄 License
This project is licensed under the MIT License.
Feel free to use, fork, modify, and share.

❤️ Support & Contributions
If you like this project, kindly ⭐ the repo. Contributions welcome — pull requests are open!

Built with 🔥 in Nigeria by a dreamer who executes.

