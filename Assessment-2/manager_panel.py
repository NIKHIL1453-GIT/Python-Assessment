from tkinter import *
from tkinter import messagebox
from models import Manager, Medicine

def manager_panel(manager_id, manager_name):
    med = Medicine()
    manager = Manager(manager_name)

    def add_med():
        name = e_name.get()
        qty = e_qty.get()
        price = e_price.get()
        if name and qty and price:
            added = med.add_medicine(name, qty, manager_id, float(price))
            if added:
                result_display.insert(END, "Medicine added successfully!\n")
        else:
            result_display.insert(END, "All fields required.\n")

    def view_meds():
        rows = med.view_medicines()
        result_display.delete(1.0, END)
        for r in rows:
            result_display.insert(END, f"{r}\n")

    def delete_med():
        med_id = e_del.get()
        if med_id:
            confirm = messagebox.askyesno("Confirm", "Are you sure to delete?")
            if confirm:
                deleted = med.delete_medicine(int(med_id))
                if deleted:
                    result_display.insert(END, "Medicine deleted successfully.\n")

    def go_back():
        root.destroy()
        import main
        main.main_menu()

    root = Tk()
    root.title("Manager Panel")
    root.geometry("600x500")

    Label(root, text=f"Welcome Manager: {manager_name}", font=("Arial", 14)).pack()

    Label(root, text="Medicine Name").pack()
    e_name = Entry(root)
    e_name.pack()

    Label(root, text="Qty").pack()
    e_qty = Entry(root)
    e_qty.pack()

    Label(root, text="Price").pack()
    e_price = Entry(root)
    e_price.pack()

    Button(root, text="Add Medicine", command=add_med).pack(pady=5)
    Button(root, text="View Medicines", command=view_meds).pack(pady=5)

    Label(root, text="Delete by Medicine ID").pack()
    e_del = Entry(root)
    e_del.pack()

    Button(root, text="Delete Medicine", command=delete_med).pack(pady=5)
    Button(root, text="Go Back", command=go_back).pack(pady=5)

    result_display = Text(root, height=10, width=60)
    result_display.pack()

    root.mainloop()
