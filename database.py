# database.py
from models import Session

# Dependency to get the database session
def get_db():
    return Session()
