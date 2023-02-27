"""
This modules handles database connection and session creation aspects
of the app.

The SQLAlchemy Object Relational Mapper presents a method of associating
user-defined Python classes with database tables, and instances of those
classes (objects) with rows in their corresponding tables. It includes a
system that transparently synchronizes all changes in state between
objects and their related rows, called a unit of work, as well as a
system for expressing database queries in terms of the user defined
classes and their defined relationships between each other.

Links:
    https://fastapi.tiangolo.com/tutorial/sql-databases/#import-the-sqlalchemy-parts
"""

from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import sessionmaker

SQLACHEMY_DATABASE_URL = "sqlite+pysqlite:///./app.db"

engine = create_engine(
    SQLACHEMY_DATABASE_URL,
    connect_args={"check_same_thread": False}
)

SessionLocal = sessionmaker(autocommit=False, autoflush=False, bind=engine)
# SessionLocal is a class that creates session objects. 
# A Session is just a workspace for your objects, local to a particular
# database connection.
# https://docs.sqlalchemy.org/en/14/orm/tutorial.html#creating-a-session
# https://docs.sqlalchemy.org/en/20/orm/session_api.html

Base = declarative_base()
# Later we will inherit from this class to create each of the database
# models or classes (the ORM models):
# When using the ORM, the configurational process starts by describing
# the database tables we’ll be dealing with, and then by defining our
# own classes which will be mapped to those tables.
# Classes mapped using the Declarative system are defined in terms of
# a base class which maintains a catalog of classes and tables relative
# to that base - this is known as the declarative base class. Our
# application will usually have just one instance of this base in a
# commonly imported module. We create the base class using the 
# declarative_base() function, as done above.

def create_metadata():
    Base.metadata.drop_all(bind=engine)    # type: ignore
    Base.metadata.create_all(bind=engine)  # type: ignore
    # NOTE: Pylance doesn't recognize the 'metadata' attribute
 #:
