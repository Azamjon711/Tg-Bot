import psycopg2 as psql
import os
from dotenv import load_dotenv
load_dotenv()


class Database:
    @staticmethod
    def connect(query, queryType):
        database = psql.connect(
            database=os.getenv("DB"),
            user=os.getenv("USER"),
            host=os.getenv("HOST"),
            password=os.getenv("PASSWORD")
        )

        cursor = database.cursor()
        cursor.execute(query)

        data = ["insert", "create", "select"]

        if queryType in data:
            database.commit()
            if queryType == "insert":
                return "Inserted"
            elif queryType == "create":
                return "created"
            elif queryType == "select":
                return cursor.fetchall()
