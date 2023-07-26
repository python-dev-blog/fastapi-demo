import os

from dotenv import load_dotenv
from fastapi import Depends
from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session

from services.group import GroupService

load_dotenv()
SQL_URL = os.environ.get("SQL_URL")

engine = create_engine(SQL_URL)
SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)


def get_db():
    db = SessionLocal()
    try:
        yield db
    finally:
        db.close()


def get_group_service(db: Session = Depends(get_db)) -> GroupService:
    return GroupService(db=db)
