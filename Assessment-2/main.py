from tkinter import *
from tkinter import messagebox
from models import Admin, Manager
import admin_panel
import manager_panel

def main_menu():
    root = Tk()
    root.title("Pharmacy Management System")
    root.geometry("400x300")

    def exit_app():
        root.destroy()

    def open_admin():
        root.destroy()
        login_register("admin")

    def open_manager():
        root.destroy()
        login_register("manager")

    Label(root, text="Welcome to Pharmacy Management", font=("Arial", 16)).pack(pady=20)

    Button(root, text="Admin", command=open_admin, width=20).pack(pady=10)
    Button(root, text="Manager", command=open_manager, width=20).pack(pady=10)
    Button(root, text="Exit", command=exit_app, width=20).pack(pady=10)

    root.mainloop()

def login_register(role):
    win = Tk()
    win.title(f"{role.capitalize()} Panel")
    win.geometry("400x300")

    Label(win, text=f"{role.capitalize()} Login/Register", font=("Arial", 14)).pack(pady=10)

    Label(win, text="Name").pack()
    e_name = Entry(win)
    e_name.pack()

    if role == "manager":
        Label(win, text="Pharmacy Name").pack()
        e_pharmacy = Entry(win)
        e_pharmacy.pack()
    else:
        e_pharmacy = None

    Label(win, text="Username").pack()
    e_user = Entry(win)
    e_user.pack()

    Label(win, text="Password").pack()
    e_pass = Entry(win, show='*')
    e_pass.pack()

    def register():
        name = e_name.get()
        username = e_user.get()
        password = e_pass.get()
        pharmacy = e_pharmacy.get() if e_pharmacy else None

        if role == "admin":
            user = Admin(name)
        else:
            user = Manager(name)

        success = user.register(username, password, pharmacy)
        if success:
            messagebox.showinfo("Success", "Registration Complete")

    def login():
        name = e_name.get()
        username = e_user.get()
        password = e_pass.get()

        if role == "admin":
            user = Admin(name)
            result = user.login(username, password)
            if result:
                win.destroy()
                admin_panel.admin_panel(result[0], name)
            else:
                messagebox.showerror("Error", "Invalid Login")
        else:
            pharmacy = e_pharmacy.get()
            user = Manager(name)
            result = user.login(username, password)
            if result:
                win.destroy()
                manager_panel.manager_panel(result[0], name)
            else:
                messagebox.showerror("Error", "Invalid Login")

    Button(win, text="Register", command=register).pack(pady=5)
    Button(win, text="Login", command=login).pack(pady=5)
    Button(win, text="Back", command=lambda: [win.destroy(), main_menu()]).pack(pady=5)

    win.mainloop()

if __name__ == "__main__":
    from init_db import initialize_tables
    initialize_tables()
    main_menu()
