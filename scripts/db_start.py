from utils.db_init import *
from sqlalchemy import create_engine
import os


uri = os.environ.get("DATABASE_URL")
engine = create_engine(uri, client_encoding="utf8")
print("Initialising database...")
initialise_database(engine)

