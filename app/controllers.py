from sqlalchemy.orm import Session
from app.models import ToDoModel
from app.schemas import ToDoBaseSchema

class ToDoController:
    @staticmethod
    def create_todo(db: Session, todo: ToDoBaseSchema):
        todo = ToDoModel(**todo.model_dump())
        db.add(todo)
        db.commit()
        return todo

    @staticmethod
    def get_todo(db: Session, id: int):
        return db.query(ToDoModel).filter(ToDoModel.id == id).first()

    @staticmethod
    def update_todo(db: Session, todo: ToDoBaseSchema, id: int):
        todo_to_update = db.query(ToDoModel).filter(ToDoModel.id == id).first()

        if todo_to_update:
            for k, v in todo.model_dump().items():
                setattr(todo_to_update, k, v)
            db.commit()
            db.refresh(todo_to_update)

        return todo_to_update

    @staticmethod
    def delete_todo(db: Session, id: int):
        todo = db.query(ToDoModel).filter(ToDoModel.id == id).first()
        if todo:
            db.delete(todo)
            db.commit()
        return todo