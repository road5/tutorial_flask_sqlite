import sys
from sqlalchemy import Column, ForeignKey, Integer, String
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy import create_engine

Base = declarative_base()   # o create a base class for declarative 
                            # class definitions and an engine for 
                            # connecting to the database using create_engine

# e create a declarative base instance called Base and define the Student class
#  as a declarative class that inherits from Base and represents the “student” 
# table
class Student(Base):
   __tablename__ = 'student'

   id = Column(Integer, primary_key=True)
   fname = Column(String(250), nullable=False)
   lname = Column(String(250), nullable=False)
   subject = Column(String(250))

engine = create_engine('sqlite:///studentList.db')
Base.metadata.create_all(engine)