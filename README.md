# Grocery Store Management System (GSMS)

A lightweight, 3-tier web application designed to manage a grocery store's inventory, products, units of measure (UOM), and customer orders. 

---

## 🚀 Architecture Overview

This project follows a classic 3-tier architecture:
1. **Frontend (Presentation Layer)**: Responsive user interface built with HTML5, CSS3, Bootstrap, jQuery, and custom JavaScript.
2. **Backend (Application Layer)**: RESTful API server built using Python 3 and Flask.
3. **Database (Data Layer)**: Relational database management using MySQL.

---

## 🛠️ Tech Stack & Requirements
* **Python** 3.8+
* **Flask** 3.x
* **MySQL Server** 8.0+
* **Dependencies**: Listed in `requirements.txt`

---

## 📂 Project Structure

```
├── backend/                   # Flask server and Database Access Objects (DAOs)
│   ├── server.py              # Main Flask server entry point (routes & static serving)
│   ├── sql_connection.py      # MySQL connection setup
│   ├── products_dao.py        # DAO for product database transactions
│   ├── orders_dao.py          # DAO for order database transactions
│   └── uom_dao.py             # DAO for Units of Measure (UOM) transactions
├── ui/                        # Web user interface assets
│   ├── css/                   # Styling sheets (Bootstrap, sidebar-menu, custom)
│   ├── js/                    # UI interactive scripts
│   │   ├── custom/            # Custom AJAX and page logic scripts
│   │   └── packages/          # Bootstrap & jQuery package dependencies
│   ├── index.html             # Dashboard page (displays and places orders)
│   ├── manage-product.html    # Product inventory management interface
│   └── order.html             # Customer order list page
├── grocery_store.sql          # MySQL database schema setup dump
├── requirements.txt           # Python backend dependencies
└── README.md                  # Project documentation
```

---

## ⚡ Setup & Installation

### 1. Clone the Repository
```bash
git clone https://github.com/your-username/grocery-store-webapp.git
cd grocery-store-webapp
```

### 2. Database Initialization
1. Ensure your local MySQL server is running.
2. Import the database schema and sample data using the provided SQL file:
   ```bash
   mysql -u root -p < grocery_store.sql
   ```
   *This creates the `grocery_store` database, establishes table relationships, and populates default UOMs and sample products.*

### 3. Backend Configuration
The database connection settings are managed securely using a `.env` file at the project root. This file is git-ignored to prevent sensitive credentials from leaking to source control.

1. Copy the template configuration file:
   ```bash
   cp .env.example .env
   ```
2. Open the newly created `.env` file and insert your actual MySQL connection details:
   ```env
   DB_HOST=localhost
   DB_USER=root
   DB_PASSWORD=your_actual_mysql_password
   DB_DATABASE=grocery_store
   ```

### 4. Install Dependencies
Install Python requirements using `pip`:
```bash
pip install -r requirements.txt
```

---

## 💻 Running the Application

1. Run the Flask server:
   ```bash
   python backend/server.py
   ```
2. Once the server is running, navigate to `http://localhost:5000` in your web browser. 

The Flask server is configured to serve both the API endpoints and the static UI assets directly.

---

## 🔒 Key Code Enhancements

* **Relative API Paths**: Frontend endpoints call relative paths (e.g., `/getProducts`), avoiding origin/CORS conflicts and making the app ready for staging or production deployment.
* **Database Graceful Failures**: The `/deleteProduct` API endpoint handles database constraint violations gracefully. If you try to delete a product that is linked to active orders, the backend returns a structured JSON error response with an HTTP `400` status, and the frontend alerts the user instead of failing silently.
