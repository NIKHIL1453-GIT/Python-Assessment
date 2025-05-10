import random
import datetime

opr_Dict = {}
sub_acc = {}
sumTotal = 0
account_no = 0 
name = "nik"
balance = 0
withdrawAmount = 0 
role_choice = True 
while role_choice:
    print("Welcome to Python BANK MANAGEMENT SYSTEM.")
    print("\n\nselect your role:")
    role_menu = """
                    1) Banker
                    2) Customer

                    3) Exit
    """
    print(role_menu)
    role = int(input("\nEnter your role"))

    if role == 1:
        opr_Status = True
        while opr_Status:
            Operation_menu = """
                Welcome to Banker's App

                                Operation menu
                                Press:
                                1) Add Customer/balance
                                2) View Customer
                                3) Search Customer
                                4) Viewall Customer
                                5) Total amount in bank 
            """
            print(Operation_menu)
            choice_opr = int(input("Enter your choice:"))
            if choice_opr == 1:
                status = True
                while status:
                    account_no = int(input("Enter account no."))
                    if account_no not in opr_Dict.keys():
                        name = input("Enter Customer's name: ").lower()
                        balance = int(input("Enter Opening Balance: "))
                        openDateTime = datetime.datetime.now()

                        # Create a new dictionary for each customer
                        sub_acc = {
                            "name": name,
                            "balance": balance,
                            "Opening-dateTime": str(openDateTime)
                        }

                        opr_Dict[account_no] = sub_acc
                        sumTotal += balance
                    elif account_no in opr_Dict.keys():
                        balance = int(input("Enter Balance: "))
                        opr_Dict[account_no]["balance"] += balance
                        sumTotal += balance
                    else:
                        print("Invalid input")

                    choice = input("Do you want to perform more add operations? Press 'y' for yes and 'n' for no: ").lower()
                    print()
                    if choice == "y" or choice == "yes":
                        status = True
                    else:
                        status = False

            elif choice_opr == 2:
                account_no = int(input("Enter account no."))
                if account_no in opr_Dict.keys():
                    print(opr_Dict[account_no]["name"])
                    print(opr_Dict[account_no]["balance"])
                else:
                    print("Invalid input.")
            elif choice_opr == 3:
                Name1 = input("Enter name:").lower()
                if Name1 == sub_acc["name"]:
                    print("valid name.")                   
                else:
                    print("not valid name.")
            elif choice_opr == 4:
                print(opr_Dict)
            elif choice_opr == 5:
                print(f"Total balance in bank: {sumTotal}") 
            else:
                opr_Status = False
    elif role == 2:
        opr_Status = True
        while opr_Status:
            customer_Menu = """ 
                            Welcome to customer App:

                                    Operations menu:
                                    Press:
                                    1) Withdraw money
                                    2) Deposit money
                                    3) View balance
            """
            print(customer_Menu)
            choice_Cust = int(input("Enter your choice:"))
            if choice_Cust == 1:
                acc_no = int(input("Enter account number:"))
                if acc_no in opr_Dict.keys():
                    print("account matched")
                    withdrawAmount = int(input("enter amount:"))
                    if withdrawAmount<opr_Dict[account_no]["balance"]:
                        sub_acc["balance"] = balance - withdrawAmount
                        sumTotal-= withdrawAmount
                    elif withdrawAmount>opr_Dict[account_no]["balance"]:
                        print("Insuffiecient balance")
                    else:
                        print("Something went wrong.")
                else:
                    print("Invalid Account number.")
            elif choice_Cust == 2:
                acc_no = int(input("Enter account number:"))
                if acc_no in opr_Dict.keys():
                    print("account matched")
                    depositAmount = int(input("enter amount:"))
                    sub_acc["balance"] = balance - withdrawAmount + depositAmount
                    sumTotal = sumTotal - withdrawAmount + depositAmount
            elif choice_Cust == 3:
                acc_no = int(input("Enter account number:"))
                if acc_no in opr_Dict.keys():
                    print("account matched")
                    print(opr_Dict[account_no]["balance"])
            else:
                print("invalid choice")
    elif role == 3:
        print("Exit from program")
        status = False
    else:
        print("invalid choice")
    
    choice = input("Do you want to perform more add operations? Press 'y' for yes and 'n' for no: ").lower()
    print()
    if choice == "y" or choice == "yes":
        status = True
    else:
        status = False