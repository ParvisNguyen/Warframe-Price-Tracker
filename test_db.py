import os
import psycopg
from dotenv import load_dotenv

# Loads database settings from .env so password is not stored in code
load_dotenv()

# Connected to PostgreSQL database running in Docker
conn = psycopg.connect(
    host = os.getenv("DB_HOST"),
    port = os.getenv("DB_PORT"),
    dbname = os.getenv ("DB_NAME"),
    user = os.getenv ("DB_USER"),
    password = os.getenv("DB_PASSWORD")
)

# The cursor sends SQL commands through the connection
cur = conn.cursor()

# Parameterized query: values sent seperately from SQL to prevent SQL injection
cur.execute(
    "INSERT INTO prices (item_slug, lowest_price) VALUES (%s ,%s)", 
    ("eternal_war", 10)
)

# Saves INSERT permanently, otherwise row is discarded if not provided
conn.commit()

print ("Inserted")
conn.close()