# models.py
import pymysql
pymysql.install_as_MySQLdb()

from sqlalchemy import Column, Integer, String, Boolean, Text
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker
from sqlalchemy import create_engine

# Create the base class for SQLAlchemy models
Base = declarative_base()

# SQLite database URL
SQLALCHEMY_DATABASE_URL = "mysql://user:password@localhost/mariadb"

# Create an engine for the SQLite database
engine = create_engine(SQLALCHEMY_DATABASE_URL)

# Create a session factory
Session = sessionmaker(autocommit=False, autoflush=False, bind=engine)

# Define the Todo model
class Todo(Base):
    __tablename__ = 'todos'

    id = Column(Integer, primary_key=True, index=True)
    title = Column(String(255), index=True)
    description = Column(Text)
    completed = Column(Boolean, default=False)

# Create the database tables
Base.metadata.create_all(bind=engine)
