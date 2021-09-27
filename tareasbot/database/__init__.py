import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Course, NRC, Assignment, User, user_nrc, Base
from..debug import Console


class Database:

    def __init__(self):
        db_uri = os.environ.get('DATABASE_URL')
        
        Console.debug_log("Connecting to Heroku Postgres", module="DATABASE")
        self.engine = create_engine(db_uri)
        
        Console.debug_log("Initialising SQLAlchemy Session factory", module="DATABASE")
        self._session = sessionmaker(bind=self.engine)
        
        Console.debug_log("Connection Successful", module="DATABASE")
        
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
