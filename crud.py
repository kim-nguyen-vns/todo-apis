# crud.py
from sqlalchemy.orm import Session
from models import Todo

# Create a new Todo item
def create_todo(db: Session, title: str, description: str):
    todo = Todo(title=title, description=description)
    db.add(todo)
    db.commit()
    db.refresh(todo)
    return todo

# Get all Todo items
def get_todos(db: Session, skip: int = 0, limit: int = 100):
    return db.query(Todo).offset(skip).limit(limit).all()

# Get a single Todo by id
def get_todo_by_id(db: Session, todo_id: int):
    return db.query(Todo).filter(Todo.id == todo_id).first()

# Update an existing Todo
def update_todo(db: Session, todo_id: int, title: str, description: str, completed: bool):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        todo.title = title
        todo.description = description
        todo.completed = completed
        db.commit()
        db.refresh(todo)
    return todo

# Delete a Todo item
def delete_todo(db: Session, todo_id: int):
    todo = db.query(Todo).filter(Todo.id == todo_id).first()
    if todo:
        db.delete(todo)
        db.commit()
    return todo
