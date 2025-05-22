import datetime
import json
import os

CUSTOMER_FILE = json.customers

def log_transaction(message):
    with open("transaction.log", "a", encoding="utf-8") as log:
        log.write(f"{datetime.datetime.now()} - {message}\n")

def load_customers():
    if not os.path.exists(CUSTOMER_FILE):
        return {}
    with open(CUSTOMER_FILE, "r", encoding="utf-8") as f:
        return json.load(f)

def save_customers(data):
    with open(CUSTOMER_FILE, "w", encoding="utf-8") as f:
        json.dump(data, f, indent=4)

opr_Dict = load_customers()

def add_customer():
    try:
        account_no = int(input("Enter account no.: "))
        if account_no not in opr_Dict:
            name = input("Enter Customer's name: ").lower()
            balance_input = input("Enter Opening Balance: ").replace(",", "").strip()
            balance = float(balance_input)

            openDateTime = datetime.datetime.now()

            sub_acc = {
                "name": name,
                "balance": balance,
                "Opening-dateTime": str(openDateTime)
            }

            opr_Dict[account_no] = sub_acc
            save_customers(opr_Dict)
            log_transaction(f"Added Customer: {account_no} - {name} - ₹{balance}")
            print("Customer added successfully.")
        else:
            print("Account already exists.")
    except ValueError as e:
        print(f"Invalid input. Error: {e}")

def view_customer():
    try:
        account_no = int(input("Enter Account Number to View: "))
        customer = opr_Dict.get(account_no)
        if customer:
            print(f"Account No: {account_no}, Name: {customer['name']}, Balance: ₹{customer['balance']}")
        else:
            print("Customer not found.")
    except ValueError:
        print("Invalid input. Please enter a valid account number.")

def search_customer():
    try:
        name = input("Enter Customer Name to Search: ").lower()
        found = False
        for account_no, data in opr_Dict.items():
            if data['name'].lower() == name:
                print(f"Account No: {account_no}, Name: {data['name']}, Balance: ₹{data['balance']}")
                found = True
        if not found:
            print("Customer not found.")
    except Exception as e:
        print(f"Error: {e}")

def view_all_customer():
    if not opr_Dict:
        print("No customers found.")
        return
    for account_no, data in opr_Dict.items():
        print(f"Account No: {account_no}, Name: {data['name']}, Balance: ₹{data['balance']}")

def total_amounts():
    total = sum(data["balance"] for data in opr_Dict.values())
    print(f"Total Amount in Bank: ₹{total}")

def delete_customer():
    try:
        account_no = int(input("Enter account number to delete: "))
        print(account_no)
        if account_no in opr_Dict:
            confirm = input(f"Are you sure you want to delete account {account_no} (y/n)? ").lower()
            if confirm == 'y':
                deleted = opr_Dict.pop(account_no)
                save_customers(opr_Dict)
                log_transaction(f"Deleted customer {account_no} - {deleted['name']}")
                print("Customer deleted successfully.")
            else:
                print("Deletion cancelled.")
        else:
            print("Account not found.")
    except ValueError:
        print("Invalid account number.")