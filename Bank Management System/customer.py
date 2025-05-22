# import banker

# def withdraw():
#     try:
#         acc_no = int(input("Enter your account number: "))
#         if acc_no in banker.opr_Dict:
#             amount = float(input("Enter amount to withdraw: "))
#             if amount <= banker.opr_Dict[acc_no]["balance"]:
#                 banker.opr_Dict[acc_no]["balance"] -= amount
#                 from banker import save_customers
#                 save_customers(banker.opr_Dict)
#                 print("Withdrawal successful.")
#                 banker.log_transaction(f"Customer {acc_no} withdrew ₹{amount}")
#             else:
#                 print("Insufficient balance.")
#                 banker.log_transaction(f"Customer {acc_no} tried to withdraw ₹{amount} - Insufficient balance")
#         else:
#             print("Account not found.")
#             banker.log_transaction(f"Withdrawal failed - Account {acc_no} not found")
#     except ValueError:
#         print("Invalid input.")

# def deposit():
#     try:
#         acc_no = int(input("Enter your account number: "))
#         if acc_no in banker.opr_Dict:
#             amount = float(input("Enter amount to deposit: "))
#             banker.opr_Dict[acc_no]["balance"] += amount
#             from banker import save_customers
#             save_customers(banker.opr_Dict)
#             print("Deposit successful.")
#             banker.log_transaction(f"Customer {acc_no} deposited ₹{amount}")
#         else:
#             print("Account not found.")
#             banker.log_transaction(f"Deposit failed - Account {acc_no} not found")
#     except ValueError:
#         print("Invalid input.")

# def view_balance():
#     try:
#         acc_no = int(input("Enter your account number: "))
#         if acc_no in banker.opr_Dict:
#             print(f"Balance: ₹{banker.opr_Dict[acc_no]['balance']}")
#             banker.log_transaction(f"Customer {acc_no} viewed balance")
#         else:
#             print("Account not found.")
#             banker.log_transaction(f"Balance check failed - Account {acc_no} not found")
#     except ValueError:
#         print("Invalid input.")