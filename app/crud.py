from sqlalchemy.orm import Session
from datetime import date
from .models import Expense
from .schemas import ExpenseCreate, ExpenseUpdate


# =========================
# CREATE
# =========================
def create_expense(db: Session, expense: ExpenseCreate):
    db_expense = Expense(**expense.dict())
    db.add(db_expense)
    db.commit()
    db.refresh(db_expense)
    return db_expense


# =========================
# READ
# =========================
def get_expenses(db: Session):
    return db.query(Expense).all()


# =========================
# UPDATE
# =========================
def update_expense(db: Session, expense_id: int, expense_data: ExpenseUpdate):
    expense = db.query(Expense).filter(
        Expense.expense_id == expense_id
    ).first()

    if not expense:
        return None

    for key, value in expense_data.dict(exclude_unset=True).items():
        setattr(expense, key, value)

    db.commit()
    db.refresh(expense)
    return expense


# =========================
# DELETE
# =========================
def delete_expense(db: Session, expense_id: int):
    expense = db.query(Expense).filter(
        Expense.expense_id == expense_id
    ).first()

    if not expense:
        return None

    db.delete(expense)
    db.commit()
    return True


# =========================
# FILTER / SEARCH
# =========================
def filter_expenses(
    db: Session,
    category: str = None,
    payment_mode: str = None,
    created_by: str = None,
    from_date: date = None,
    to_date: date = None
):
    query = db.query(Expense)

    if category:
        query = query.filter(Expense.category == category)

    if payment_mode:
        query = query.filter(Expense.payment_mode == payment_mode)

    if created_by:
        query = query.filter(Expense.created_by == created_by)

    if from_date and to_date:
        query = query.filter(Expense.date.between(from_date, to_date))

    return query.all()
