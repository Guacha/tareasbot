import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker
from .models import Course, NRC, Assignment, User, user_nrc, Base
from ..debug import Console


class Database:
    """
    A handler for the PosgreSQL database. In order for this class to work, there should be special environment variables
    specifying the database configuration and access
    """

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
        """
        Method to initialise database and create all tables
        Warnings:
            This method should only be called once and not as a part of the bot's operation
        """
        Base.metadata.create_all(self.engine)

    def add_course(self, course_dept: str, course_code: int, course_name: str, course_semester: int) -> bool:

        s = self._session()
        try:
            c = Course(
                name=course_name,
                course_dept=course_dept,
                course_code=course_code,
                semester_code=course_semester
            )
            self.console.log("Adding course to database...")
            s.add(c)
            s.commit()
            self.console.debug_log(f"Course added: {c}")
            return True
        except Exception as e:
            return False

    def get_courses(self):
        self.console.debug_log("Querying for all courses...")
        s = self._session()
        courses = s.query(Course).all()
        self.console.log(f"Query completed. Got {len(courses)} results.")
        return courses

    def get_duplicate_course(self, dept: str, code: int):
        self.console.debug_log("Querying for duplicate course with dept {dept} and code {code}")
