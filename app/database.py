from sqlalchemy import create_engine          # Imports function to create a database engine
from sqlalchemy.orm import sessionmaker       # Imports session factory for database operations

DATABASE_URL = "sqlite:///./expenses.db"      # Defines SQLite database file location

engine = create_engine(                       # Creates database engine
    DATABASE_URL,                             # Uses the defined database URL
    connect_args={"check_same_thread": False} # Allows SQLite to be used with multiple threads
)

SessionLocal = sessionmaker(                  # Creates a database session generator
    bind=engine                               # Binds sessions to the database engine
)
