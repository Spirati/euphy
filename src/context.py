import os
import mysql.connector

class DatabaseConnection():
    def __enter__(self):
        self.connection = mysql.connector.connect(
            host="db",
            user="euphy",
            password=os.getenv("EUPHYDB_USER_PASS"),
            database="euphy"
        )
        self.cursor = self.connection.cursor()

        return self.cursor
    def __exit__(self, type, value, traceback):
        self.cursor.fetchall()
        self.cursor.close()