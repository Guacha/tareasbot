import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Course, NRC, Assignment, User, user_nrc, Base

class Database():

    def __init__(self):
        DB_URI = os.environ.get('DATABASE_URL')
        self.engine = create_engine(DB_URI)
        self._session = sessionmaker(bind=self.engine)
        
    def get_session(self):
        return self._session()
    
    def initialise_db(self):
        Base.metadata.create_all(self.engine)
        
    def add_course(self, course):
        s = self._session()
        s.add(course)
        s.commit()
        
    def get_courses(self):
        s = self._session()
        courses = s.query(Course).all()
        return courses
            
    
db = Database()
