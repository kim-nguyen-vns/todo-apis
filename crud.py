# crud.py
from sqlalchemy.orm import Session
from models import Todo

# Create a new Todo item
def create_todo(db: Session, title: str, description: str):
    db_todo = Todo(title=title, description=description)
    db.add(db_todo)
    db.commit()
    db.refresh(db_todo)
    return db_todo

# Get all Todo items
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()

# Get a single Todo by id
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

# Update an existing Todo
def update_todo(db: Session, todo_id: int, title: str, description: str, completed: bool):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db_todo.title = title
        db_todo.description = description
        db_todo.completed = completed
        db.commit()
        db.refresh(db_todo)
    return db_todo

# Delete a Todo item
def delete_todo(db: Session, todo_id: int):
    db_todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if db_todo:
        db.delete(db_todo)
        db.commit()
    return db_todo
