import os

from sqlalchemy import create_engine
from dotenv import load_dotenv
from sqlalchemy.orm import sessionmaker

load_dotenv()


# Database connection setup 

url = os.getenv("DATABASE_URL")

engine = create_engine(url)

SessionLocal = sessionmaker(
    bind=engine,
    autoflush=False,
    autocommit=False
)


# get database access

def get_db():
    db = SessionLocal()

    try:
        yield db
    finally:
        db.close()