from tkinter import *
from models import Admin

def admin_panel(admin_id, admin_name):
    def view_managers():
        result = admin.view_all_managers()
        display.delete(1.0, END)
        for row in result:
            display.insert(END, f"{row}\n")

    def view_medicines():
        result = admin.view_all_medicines()
        display.delete(1.0, END)
        for row in result:
            display.insert(END, f"{row}\n")

    def go_back():
        root.destroy()
        import main
        main.main_menu()

    admin = Admin(admin_name)

    root = Tk()
    root.title("Admin Panel")
    root.geometry("500x400")

    Label(root, text=f"Welcome Admin: {admin_name}", font=("Arial", 14)).pack()

    Button(root, text="View All Managers", command=view_managers).pack(pady=10)
    Button(root, text="View All Medicines", command=view_medicines).pack(pady=10)
    Button(root, text="Go Back", command=go_back).pack(pady=10)

    display = Text(root, height=15, width=60)
    display.pack()

    root.mainloop()
