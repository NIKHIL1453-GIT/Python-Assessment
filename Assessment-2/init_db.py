import pymysql
from db_config import Database

def create_database_if_not_exists():
    try:
        connection = pymysql.connect(
            host="localhost",
            user="root",
            password="",
            port=3307
        )
        cursor = connection.cursor()
        cursor.execute("CREATE DATABASE IF NOT EXISTS pharmacy_db")
        connection.commit()
        connection.close()
        print("Database 'pharmacy_db' created or already exists.")
    except Exception as e:
        print("Failed to create database:", e)

def initialize_tables():
    db = Database()
    cursor = db.get_cursor()

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS admins (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS managers (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        pharmacy_name VARCHAR(100),
        username VARCHAR(50) UNIQUE,
        password VARCHAR(50)
    )""")

    cursor.execute("""
    CREATE TABLE IF NOT EXISTS medicines (
        id INT PRIMARY KEY AUTO_INCREMENT,
        name VARCHAR(100),
        qty VARCHAR(50),
        added_date VARCHAR(20),
        added_by INT,
        price FLOAT
    )""")

    db.commit()
    print("All tables initialized successfully.")

if __name__ == "__main__":
    create_database_if_not_exists()
    initialize_tables()
