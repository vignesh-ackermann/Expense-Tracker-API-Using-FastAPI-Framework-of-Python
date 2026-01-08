from fastapi import FastAPI

from .models import Base
from .database import engine
from .routes import router as main_router
from .reports import router as reports_router


# =========================
# DATABASE INITIALIZATION
# =========================
Base.metadata.create_all(bind=engine)


# =========================
# FASTAPI APP INITIALIZATION
# =========================
app = FastAPI(title="Expense Tracker API")


# =========================
# ROUTER REGISTRATION
# =========================
app.include_router(main_router)
app.include_router(reports_router)


# =========================
# ROOT ENDPOINT
# =========================
@app.get("/")
def root():
    return {"status": "Expense Tracker API is running"}
