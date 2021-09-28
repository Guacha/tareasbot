from sqlalchemy import Column, String, Integer, ForeignKey, DateTime, Table, UniqueConstraint
from sqlalchemy.orm import relationship
from sqlalchemy.ext.declarative import declarative_base

Base = declarative_base()

user_nrc = Table('user_nrc', Base.metadata,
                 Column('user_id', ForeignKey('users.id'), primary_key=True),
                 Column('nrc_id', ForeignKey('nrcs.id'), primary_key=True)
                 )


class User(Base):
    __tablename__ = "users"
    id = Column(Integer, primary_key=True)
    enrolled_nrcs = relationship("NRC", secondary=user_nrc, back_populates="enrolled_users")


class Course(Base):
    __tablename__ = 'courses'
    __table_args__ = (UniqueConstraint('course_dept', 'course_code', name="_course_dept_course_semester_uc"),)
    id = Column(Integer, primary_key=True)
    course_dept = Column(String(5), nullable=False)
    course_code = Column(String(5), nullable=False)
    name = Column(String(150), nullable=False)
    nrcs = relationship("NRC", back_populates="course")

    def __repr__(self):
        return f"<Course: {self.name} ({self.course_dept} {self.course_code})>"


class NRC(Base):
    __tablename__ = 'nrcs'
    __table_args__ = (UniqueConstraint('nrc', 'semester_code', name="_nrc_semester_uc"),)
    id = Column(Integer, primary_key=True)
    nrc = Column(Integer, nullable=False)
    semester_code = Column(Integer, nullable=False)
    course_id = Column(Integer, ForeignKey("courses.id"))
    course = relationship("Course", back_populates="nrcs")
    assignments = relationship("Assignment", back_populates="nrc")
    enrolled_users = relationship("User", secondary=user_nrc, back_populates="enrolled_nrcs")

    def __repr__(self):
        return f"<NRC: {self.id:04} for course {self.course.course_dept} {self.course.course_code}>"


class Assignment(Base):
    __tablename__ = "assignments"
    id = Column(Integer, primary_key=True)
    nrc_id = Column(Integer, ForeignKey("nrcs.id"))
    nrc = relationship("NRC", back_populates="assignments")
    name = Column(String(255), nullable=False)
    due_date = Column(DateTime, nullable=False)
