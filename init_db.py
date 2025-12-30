import psycopg2
from psycopg2 import sql

DB_NAME = "telejournalism_db"
DB_USER = "postgres" 
DB_PASSWORD = "maria07" 
DB_HOST = "localhost"

conn = psycopg2.connect(dbname="postgres", user=DB_USER, password=DB_PASSWORD, host=DB_HOST)
conn.autocommit = True  
cur = conn.cursor()

try:
    cur.execute(sql.SQL("CREATE DATABASE {} OWNER {}").format(
        sql.Identifier(DB_NAME),
        sql.Identifier(DB_USER)
    ))
    print(f"Database '{DB_NAME}' created successfully.")
except Exception as e:
    print(f"Error: {e}")

cur.close()
conn.close()


