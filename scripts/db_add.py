from utils.db_fill import fill_courses
from sqlalchemy import create_engine
import os

uri = os.environ.get("DATABASE_URL")
engine = create_engine(uri, client_encoding="utf8")
fill_courses("courses.csv")
