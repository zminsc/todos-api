from fastapi import APIRouter, Depends
from sqlalchemy.orm import Session
from app.database import get_db
from app.schemas import ToDoSchema, ToDoBaseSchema
from app.controllers import ToDoController

router = APIRouter()

@router.post("/todos/", response_model=ToDoSchema)
def create_todo(todo: ToDoBaseSchema, db: Session = Depends(get_db)):
    return ToDoController.create_todo(db, todo)

@router.get("/todos/{id}", response_model=ToDoSchema)
def read_todo(id: int, db: Session = Depends(get_db)):
    return ToDoController.get_todo(db, id)

@router.put("/todos/{id}", response_model=ToDoSchema)
def update_todo(id: int, todo: ToDoBaseSchema, db: Session = Depends(get_db)):
    return ToDoController.update_todo(db, id, todo)

@router.delete("/todos/{todo_id}", response_model=ToDoSchema)
def delete_todo(id: int, db: Session = Depends(get_db)):
    return ToDoController.delete_todo(db, id)