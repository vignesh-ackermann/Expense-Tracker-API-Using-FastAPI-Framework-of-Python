Expense Tracker API

A robust and scalable Expense Tracker REST API built using the FastAPI framework in Python.
This project enables users to manage expenses efficiently, generate category-based summaries, and export expense reports in PDF and Excel formats.

🚀 Features

Create, read, update, and delete expenses (CRUD)

Category-wise expense aggregation

Downloadable PDF expense reports

Downloadable Excel (XLSX) expense reports

SQLAlchemy ORM for database interaction

FastAPI dependency injection & validation

Clean, modular, and production-ready architecture

🛠️ Tech Stack
Layer	Technology
Backend Framework	FastAPI
Language	Python 3.9+
ORM	SQLAlchemy
Database	SQLite / PostgreSQL (configurable)
PDF Generation	ReportLab
Excel Export	OpenPyXL
API Docs	Swagger UI (OpenAPI)
Server	Uvicorn


📁 Project Structure
app/
├── main.py              # FastAPI application entry point
├── database.py          # Database connection & engine
├── models.py            # SQLAlchemy models
├── crud.py              # Database operations
├── routes.py            # Expense CRUD APIs
├── reports.py           # PDF & Excel report generation
├── schemas.py           # Pydantic schemas (if applicable)
└── __init__.py

⚙️ Installation & Setup
1️⃣ Clone the Repository
git clone https://github.com/your-username/expense-tracker-api.git
cd expense-tracker-api

2️⃣ Create Virtual Environment
python -m venv venv
source venv/bin/activate   # Windows: venv\Scripts\activate

3️⃣ Install Dependencies
pip install -r requirements.txt

4️⃣ Run the Application
uvicorn app.main:app --reload

🌐 API Documentation

Once the server is running:

Swagger UI → http://127.0.0.1:8000/docs

ReDoc → http://127.0.0.1:8000/redoc

These interfaces allow you to test all APIs interactively.


📌 API Endpoints
Expense APIs
Method	Endpoint	Description
POST	/expenses/	Create a new expense
GET	/expenses/	Get all expenses
GET	/expenses/{id}	Get expense by ID
PUT	/expenses/{id}	Update expense
DELETE	/expenses/{id}	Delete expense
Report APIs
Method	Endpoint	Description
GET	/reports/pdf	Download expense report (PDF)
GET	/reports/excel	Download expense report (Excel)



📄 Sample Expense Fields

Date

Category

Amount

Merchant Name

Description (optional)

📊 Reports Module

PDF Report

Multi-page support

Clean layout with headers

In-memory streaming (no file storage)

Excel Report

Structured tabular format

Ready for financial analysis

Compatible with MS Excel & Google Sheets

🔐 Future Enhancements

JWT authentication & authorization

User-based expense tracking

Date-range and category filters

Cloud database integration

Docker support

Deployment on AWS / Azure

🧪 Testing (Optional)
pytest

📜 License

This project is licensed under the MIT License.

👤 Author

Vignesh Kumar
Python Full stack Developer
