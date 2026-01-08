from io import BytesIO

from fastapi import APIRouter, Depends
from fastapi.responses import StreamingResponse
from sqlalchemy import func
from sqlalchemy.orm import Session

from reportlab.lib.pagesizes import A4
from reportlab.pdfgen import canvas
from openpyxl import Workbook

from .database import SessionLocal
from .models import Expense
from .crud import get_expenses


# =========================
# ROUTER INITIALIZATION
# =========================
router = APIRouter(
    prefix="/reports",
    tags=["Reports"]
)


# =========================
# DB DEPENDENCY
# =========================
def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


# =========================
# CATEGORY SUMMARY
# =========================
def category_summary(db: Session):
    return (
        db.query(
            Expense.category,
            func.sum(Expense.amount).label("total_amount")
        )
        .group_by(Expense.category)
        .all()
    )


# =========================
# PDF REPORT (IN-MEMORY)
# =========================
def generate_pdf(expenses):
    buffer = BytesIO()
    pdf = canvas.Canvas(buffer, pagesize=A4)

    width, height = A4

    def draw_header(y_pos):
        pdf.setFont("Helvetica-Bold", 14)
        pdf.drawString(40, y_pos, "Expense Report")

        y_pos -= 30
        pdf.setFont("Helvetica-Bold", 10)
        pdf.drawString(40, y_pos, "Date | Category | Amount | Merchant")
        return y_pos - 20

    y = height - 40
    y = draw_header(y)
    pdf.setFont("Helvetica", 10)

    for expense in expenses:
        line = (
            f"{expense.date.strftime('%Y-%m-%d')} | "
            f"{expense.category} | "
            f"₹{expense.amount:.2f} | "
            f"{expense.merchant_name or ''}"
        )

        pdf.drawString(40, y, line)
        y -= 18

        if y < 40:
            pdf.showPage()
            y = height - 40
            y = draw_header(y)
            pdf.setFont("Helvetica", 10)

    pdf.save()
    buffer.seek(0)
    return buffer


# =========================
# EXCEL REPORT (IN-MEMORY)
# =========================
def generate_excel(expenses):
    wb = Workbook()
    ws = wb.active
    ws.title = "Expenses"

    ws.append(["Date", "Category", "Amount", "Merchant"])

    for e in expenses:
        ws.append([
            e.date.strftime('%Y-%m-%d'),
            e.category,
            float(e.amount),
            e.merchant_name or ""
        ])

    buffer = BytesIO()
    wb.save(buffer)
    buffer.seek(0)
    return buffer


# =========================
# DOWNLOAD PDF REPORT
# =========================
@router.get("/pdf")
def download_expense_pdf(db: Session = Depends(get_db)):
    expenses = get_expenses(db)
    pdf_buffer = generate_pdf(expenses)

    return StreamingResponse(
        pdf_buffer,
        media_type="application/pdf",
        headers={
            "Content-Disposition": "attachment; filename=expense_report.pdf"
        }
    )


# =========================
# DOWNLOAD EXCEL REPORT
# =========================
@router.get("/excel")
def download_expense_excel(db: Session = Depends(get_db)):
    expenses = get_expenses(db)
    excel_buffer = generate_excel(expenses)

    return StreamingResponse(
        excel_buffer,
        media_type="application/vnd.openxmlformats-officedocument.spreadsheetml.sheet",
        headers={
            "Content-Disposition": "attachment; filename=expense_report.xlsx"
        }
    )
