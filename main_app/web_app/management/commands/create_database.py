from django.core.management.base import BaseCommand
import psycopg2
from main_app.settings import os
from psycopg2 import sql


class Psql:
    
    def __init__(self, pool):
        self.pool = pool

    @classmethod
    def connect_postgres(self):
        try:
            conn = psycopg2.connect(
                dbname="postgres",
                user=os.getenv("POSTGRES_USER"),
                password=os.getenv("POSTGRES_PASSWORD"),
                host=os.getenv("POSTGRES_HOST"),
                port=os.getenv("POSTGRES_PORT"),
            )
            conn.autocommit = True
            return self(conn)
        except (psycopg2.DatabaseError, Exception) as error:
            print(error)

    def close_postgres(self):
        self.pool.close()

    def create_db(self):
        try:
            cur = self.pool.cursor()
            cur.execute(sql.SQL(f"CREATE DATABASE {os.getenv("POSTGRES_DBNAME")}"))
            cur.close()
        except psycopg2.errors.DuplicateDatabase as error:
            print(error, f'\nDatabase "{os.getenv("POSTGRES_DBNAME")}" is existed')
        except Exception as e:
            print(e)



class Command(BaseCommand):
    """
    Create database command
    
    """
    def handle(self, *args, **kwargs):
        connection = Psql.connect_postgres()
        connection.create_db()
        connection.close_postgres()