from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_nrc = Table('user_nrc', Base.metadata,
                 Column('user_id', ForeignKey('user.id'), primary_key=True),
                 Column('nrc_id', ForeignKey('nrc.id'), primary_key=True)
                )

class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    enrolled_nrcs = relationship("NRC", secondary=user_nrc, back_populates="enrolled_users")

class Course(Base):
    __tablename__ = 'courses'
    id = Column(Integer, primary_key=True)
    course_dept = Column(String(5), nullable=False)
    course_code = Column(Integer(5), nullable=False)
    name = Column(String(150), nullable=False)
    nrcs = relationship("NRC", back_populates="course")
    semester_code = Column(Integer(6), nullable=False)
    
    def __repr__(self):
        return f"Course: {self.name} ({self.id})"
    
class NRC(Base):
    __tablename__ = 'nrcs'
    id = Column(Integer, primary_key=True)
    course_id = Column(Integer, ForeignKey("course.id"))
    course = relationship("Course", back_populates="nrcs")
    assignments = relationship("Assignment", back_populates="nrc")
    enrolled_users = relationship("User", secondary=user_nrc, back_populates="enrolled_nrcs")
    
class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    nrc_id = Column(Integer, ForeignKey("nrc.id"))
    nrc = relationship("NRC", back_populates="assignments")
    name = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=False)
    