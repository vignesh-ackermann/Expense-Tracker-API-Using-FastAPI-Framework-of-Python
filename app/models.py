from sqlalchemy import Column, Integer, String, Float, Date   # Imports column types used in the table
from sqlalchemy.ext.declarative import declarative_base       # Imports base class for ORM models

Base = declarative_base()                                     # Creates a base class for all ORM models

class Expense(Base):                                         # Defines Expense table model
    __tablename__ = "expenses"                               # Specifies database table name

    expense_id = Column(Integer, primary_key=True, index=True)  # Unique identifier for each expense
    date = Column(Date)                                      # Stores the date of the expense
    category = Column(String)                                # Stores expense category (e.g., Food, Travel)
    amount = Column(Float)                                   # Stores expense amount
    description = Column(String)                             # Stores expense description/details
    payment_mode = Column(String)                            # Stores payment method (Cash, Card, UPI)
    merchant_name = Column(String)                            # Stores merchant or vendor name
    location = Column(String)                                 # Stores place where expense occurred
    notes = Column(String)                                    # Stores additional notes or remarks
    created_by = Column(String)                               # Stores name/ID of the user who created the entry
