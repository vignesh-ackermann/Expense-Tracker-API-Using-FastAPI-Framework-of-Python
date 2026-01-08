from pydantic import BaseModel
from typing import Optional
import datetime


class ExpenseCreate(BaseModel):
    date: datetime.date
    category: str
    amount: float
    description: Optional[str] = None
    payment_mode: Optional[str] = None
    merchant_name: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    created_by: Optional[str] = None


class ExpenseUpdate(BaseModel):
    date: Optional[datetime.date] = None
    category: Optional[str] = None
    amount: Optional[float] = None
    description: Optional[str] = None
    payment_mode: Optional[str] = None
    merchant_name: Optional[str] = None
    location: Optional[str] = None
    notes: Optional[str] = None
    created_by: Optional[str] = None


class ExpenseResponse(ExpenseCreate):
    expense_id: int

    class Config:
        from_attributes = True
