import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Course, NRC, Assignment, User, user_nrc, Base
from..debug import Console


class Database:

    def __init__(self):
        self.console = Console("DATABASE")
        db_uri = os.environ.get('DATABASE_URL')
        
        self.console.debug_log("Connecting to Heroku Postgres")
        self.engine = create_engine(db_uri)
        
        self.console.debug_log("Initialising SQLAlchemy Session factory")
        self._session = sessionmaker(bind=self.engine)
        
        self.console.debug_log("Connection Successful")
        
    def get_session(self):
        return self._session()
    
    def initialise_db(self):
        Base.metadata.create_all(self.engine)
        
    def add_course(self, course):
        s = self._session()
        s.add(course)
        s.commit()
        
    def get_courses(self):
        self.console.debug_log("Querying for all courses...")
        s = self._session()
        courses = s.query(Course).all()
        self.console.log(f"Query completed. Got {len(courses)} results.")
        return courses
