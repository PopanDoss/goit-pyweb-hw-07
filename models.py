from datetime import datetime

from sqlalchemy import Column, Integer, String, Boolean
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy.orm import relationship
from sqlalchemy.sql.schema import ForeignKey, Table
from sqlalchemy.sql.sqltypes import DateTime


Base = declarative_base()


class Groups(Base):
    __tablename__ = "groups"

    group_id  = Column(Integer, primary_key=True)
    group_name = Column(String, nullable=False)

    students = relationship("Students", back_populates="group")

class Students(Base):
    __tablename__ = "students"

    student_id  = Column(Integer, primary_key=True)
    student_name = Column(String, nullable=False)
    group_id = Column (Integer, ForeignKey("groups.group_id"))

    group = relationship("Groups", back_populates="students")

class Teachers(Base):
    __tablename__ ="teachers"

    teacher_id = Column(Integer, primary_key=True,)
    teacher_name = Column(String, nullable=False)

    

class Subjects(Base):
    __tablename__ = "subjects"

    subject_id  = Column(Integer, primary_key=True)
    subject_name = Column(String, nullable=False)
    teacher_id = Column (Integer, ForeignKey("teachers.teacher_id") )
    
    teacher_name = relationship("Teachers", backref="subjects")

class Magazine(Base):
    __tablename__ = "magazine"

    id = Column(Integer, primary_key=True)
    subject_id = Column(Integer, ForeignKey(Subjects.subject_id))
    student_id = Column(Integer, ForeignKey(Students.student_id))
    rating = Column(Integer)
    created_at = Column(DateTime, default=datetime.now())
