import pymysql

class Database:
    def __init__(self):
        try:
            self.connection = pymysql.connect(
                host="localhost",
                user="root",
                password="",
                database="pharmacy_db",
                port=3307
            )
            self.cursor = self.connection.cursor()
        except Exception as e:
            print("Database connection failed:", e)

    def get_connection(self):
        return self.connection

    def get_cursor(self):
        return self.cursor

    def commit(self):
        self.connection.commit()

    def close(self):
        self.cursor.close()
        self.connection.close()
