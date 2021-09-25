import os
import psycopg2

#DB_URL = os.environ["DATABASE_URL"]

conn = psycopg2.connect(host="localhost", port=5432, sslmode="require")