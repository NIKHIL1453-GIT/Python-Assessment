from db_config import Database
import datetime

class User:
    def __init__(self, name, role):
        self.name = name
        self.role = role
        self.db = Database()
        self.cursor = self.db.get_cursor()

    def register(self, username, password, pharmacy_name=None):
        try:
            if self.role == "admin":
                self.cursor.execute("INSERT INTO admins (name, username, password) VALUES (%s, %s, %s)",
                                    (self.name, username, password))
            elif self.role == "manager":
                self.cursor.execute("INSERT INTO managers (name, pharmacy_name, username, password) VALUES (%s, %s, %s, %s)",
                                    (self.name, pharmacy_name, username, password))
            self.db.commit()
            return True
        except Exception as e:
            print("Registration Error:", e)
            return False

    def login(self, username, password):
        try:
            if self.role == "admin":
                self.cursor.execute("SELECT * FROM admins WHERE username=%s AND password=%s", (username, password))
            elif self.role == "manager":
                self.cursor.execute("SELECT * FROM managers WHERE username=%s AND password=%s", (username, password))
            result = self.cursor.fetchone()
            return result
        except Exception as e:
            print("Login Error:", e)
            return None

class Medicine:
    def __init__(self):
        self.db = Database()
        self.cursor = self.db.get_cursor()

    def add_medicine(self, name, qty, added_by, price):
        try:
            today = datetime.date.today().strftime("%d/%m/%Y")
            self.cursor.execute("INSERT INTO medicines (name, qty, added_date, added_by, price) VALUES (%s, %s, %s, %s, %s)",
                                (name, qty, today, added_by, price))
            self.db.commit()
            return True
        except Exception as e:
            print("Add Medicine Error:", e)
            return False

    def view_medicines(self):
        self.cursor.execute("SELECT * FROM medicines")
        return self.cursor.fetchall()

    def delete_medicine(self, med_id):
        try:
            self.cursor.execute("DELETE FROM medicines WHERE id=%s", (med_id,))
            self.db.commit()
            return True
        except Exception as e:
            print("Delete Error:", e)
            return False

class Admin(User):
    def __init__(self, name):
        super().__init__(name, "admin")

    def view_all_managers(self):
        self.cursor.execute("SELECT id, name, pharmacy_name FROM managers")
        return self.cursor.fetchall()

    def view_all_medicines(self):
        self.cursor.execute("SELECT * FROM medicines")
        return self.cursor.fetchall()

class Manager(User):
    def __init__(self, name):
        super().__init__(name, "manager")
        self.__qty = 0

    def set_qty(self, qty):
        self.__qty = qty

    def get_qty(self):
        return self.__qty
