from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
import os

# Use SQLite for local testing if DATABASE_URL is not set
DATABASE_URL = os.getenv(
    "DATABASE_URL",
    "sqlite:///./tasktracker.db"  # Default to SQLite for testing
)

# For PostgreSQL in production/Docker
if DATABASE_URL.startswith("postgresql"):
    engine = create_engine(DATABASE_URL)
else:
    # SQLite settings
    engine = create_engine(
        DATABASE_URL,
        connect_args={"check_same_thread": False}  # Only needed for SQLite
    )

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)

Base = declarative_base()
