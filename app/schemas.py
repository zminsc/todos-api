from pydantic import BaseModel

class ToDoBaseSchema(BaseModel):
    title: str
    description: str
    completed: bool = False

class ToDoSchema(ToDoBaseSchema):
    id: int

    class Config:
        from_attributes = True