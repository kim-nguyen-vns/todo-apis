# main.py
from fastapi import FastAPI, Depends, HTTPException
from sqlalchemy.orm import Session
from database import get_db
import crud

app = FastAPI()

# Create a Todo item
@app.post("/todos/")
def create_todo(title: str, description: str, db: Session = Depends(get_db)):
    return crud.create_todo(db=db, title=title, description=description)

# Read all Todo items
@app.get("/todos/")
def get_todos(skip: int = 0, limit: int = 100, db: Session = Depends(get_db)):
    todos = crud.get_todos(db=db, skip=skip, limit=limit)
    return todos

# Read a specific Todo item by ID
@app.get("/todos/{todo_id}")
def get_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.get_todo_by_id(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Update a Todo item by ID
@app.put("/todos/{todo_id}")
def update_todo(todo_id: int, title: str, description: str, completed: bool, db: Session = Depends(get_db)):
    db_todo = crud.update_todo(db=db, todo_id=todo_id, title=title, description=description, completed=completed)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return db_todo

# Delete a Todo item by ID
@app.delete("/todos/{todo_id}")
def delete_todo(todo_id: int, db: Session = Depends(get_db)):
    db_todo = crud.delete_todo(db=db, todo_id=todo_id)
    if db_todo is None:
        raise HTTPException(status_code=404, detail="Todo not found")
    return {"message": "Todo deleted successfully"}
