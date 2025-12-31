import psycopg2
from psycopg2.extensions import ISOLATION_LEVEL_AUTOCOMMIT
import os

DB_NAME = "telejournalism_db"
DB_USER = "postgres"
DB_PASSWORD = "maria07"
DB_HOST = "localhost"
DB_PORT = "5432"

def main():
    conn = psycopg2.connect(
        dbname="postgres",
        user=DB_USER,
        password=DB_PASSWORD,
        host=DB_HOST,
        port=DB_PORT
    )

    conn.set_isolation_level(ISOLATION_LEVEL_AUTOCOMMIT)
    cursor = conn.cursor()

    cursor.execute(f"""
        SELECT 1 FROM pg_database WHERE datname = '{DB_NAME}'
    """)
    exists = cursor.fetchone()

    if not exists:
        cursor.execute(f'CREATE DATABASE {DB_NAME} OWNER {DB_USER}')
        print(f"Database '{DB_NAME}' created.")
    else:
        print(f"Database '{DB_NAME}' already exists.")

    cursor.close()
    conn.close()


if __name__ == "__main__":
    main()
