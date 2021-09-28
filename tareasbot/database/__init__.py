import os

from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker, Session
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
        self.engine = create_engine(db_uri, client_encoding='utf8')

        self.console.debug_log("Initialising SQLAlchemy Session factory")
        self._session = sessionmaker(bind=self.engine)

        self.console.debug_log("Connection Successful")

    def get_session(self) -> Session:
        """
        Gets a valid session object to interact with the database through Object Relational Mapping

        Returns: A session object

        """
        return self._session()

    def add_course(self, course_dept: str, course_code: str, course_name: str) -> bool:
        """
        Add a new course to the Database with given parameters

        Args:
            course_dept: The course department. A 3-4 letter string
            course_code: The course code. a 4-5 digit string
            course_name: The course name.

        Returns: A boolean representing if the transaction was successful

        """
        s = self._session()
        try:
            c = Course(
                name=course_name,
                course_dept=course_dept,
                course_code=course_code
            )
            self.console.log("Adding course to database...")
            s.add(c)
            s.commit()
            self.console.debug_log(f"Course added: {c}")
            return True
        except Exception as e:
            self.console.err(f"Error in adding course: {e}")
            return False

    def get_courses(self) -> list[Course]:
        self.console.debug_log("Querying for all courses...")
        s = self._session()
        courses = s.query(Course).all()
        self.console.log(f"Query completed. Got {len(courses)} results.")
        return courses

    def get_course(self, dept: str, code: str) -> Course:
        dept = dept.upper()
        self.console.debug_log(f"Querying to find course {dept} {code}")

        query = self.get_session().query(Course).filter_by(course_dept=dept, course_code=code)

        return query.first()
