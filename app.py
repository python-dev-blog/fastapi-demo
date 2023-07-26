import os
from typing import List

import uvicorn
from dotenv import load_dotenv
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session

from dependencies import get_db, get_group_service
from models import Group
from schemas.inputs import GroupCreate
from schemas.reponse import GroupResponse, StudentResponse
from services.group import GroupService


app = FastAPI()


@app.get("/groups/", response_model=List[GroupResponse])
def get_groups(offset: int = 0, limit: int = 10, db: Session = Depends(get_db)):
    return db.query(Group).offset(offset).limit(limit).all()


@app.get("/groups/{group_id}/", response_model=GroupResponse)
def get_group(group_id: int, db: Session = Depends(get_db)):
    return db.query(Group).filter(Group.id == group_id).first()


@app.get("/groups/{group_id}/students/", response_model=List[StudentResponse])
def get_students_by_group(group_id: int, db: Session = Depends(get_db)):
    group = db.query(Group).filter(Group.id == group_id).first()
    if not group:
        raise HTTPException(status_code=404, detail="Группа не найдена")
    return group.students


@app.post("/groups/", response_model=GroupResponse)
def create_group(group: GroupCreate, group_service: GroupService = Depends(get_group_service)):
    return group_service.create_group(group)


if __name__ == '__main__':
    uvicorn.run(app, host="localhost", port=8002)
