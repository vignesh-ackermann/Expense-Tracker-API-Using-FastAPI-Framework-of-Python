from fastapi import APIRouter, Depends, HTTPException
from sqlalchemy.orm import Session
from typing import List

from .database import SessionLocal
from . import crud, schemas


router = APIRouter(
    prefix="/expenses",
    tags=["Expenses"]
)


# =========================
# DATABASE DEPENDENCY
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CREATE
# =========================
@router.post("/", response_model=schemas.ExpenseResponse)
def add_expense(
    expense: schemas.ExpenseCreate,
    db: Session = Depends(get_db)
):
    return crud.create_expense(db, expense)


# =========================
# READ
# =========================
@router.get("/", response_model=List[schemas.ExpenseResponse])
def list_expenses(
    db: Session = Depends(get_db)
):
    return crud.get_expenses(db)


# =========================
# UPDATE
# =========================
@router.put("/{expense_id}", response_model=schemas.ExpenseResponse)
def update_expense(
    expense_id: int,
    expense: schemas.ExpenseUpdate,
    db: Session = Depends(get_db)
):
    updated = crud.update_expense(db, expense_id, expense)
    if not updated:
        raise HTTPException(status_code=404, detail="Expense not found")
    return updated


# =========================
# DELETE
# =========================
@router.delete("/{expense_id}")
def delete_expense(
    expense_id: int,
    db: Session = Depends(get_db)
):
    deleted = crud.delete_expense(db, expense_id)
    if not deleted:
        raise HTTPException(status_code=404, detail="Expense not found")
    return {"message": "Expense deleted successfully"}
