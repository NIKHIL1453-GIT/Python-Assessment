# import banker
# import customer

# def banker_menu():
#     opr_Status = True
#     while opr_Status:
#         Operation_menu = """
#         Welcome to Banker's App

#                 Operation menu
#                 Press:
#                 1) Add Customer/balance
#                 2) View Customer
#                 3) Search Customer
#                 4) View All Customers
#                 5) Total amount in bank
#                 6) Delete Customer
#                 7) Back to main menu
#         """
#         print(Operation_menu)
#         try:
#             choice_opr = int(input("Enter your choice: "))
#             if choice_opr == 1:
#                 banker.add_customer()
#             elif choice_opr == 2:
#                 banker.view_customer()
#             elif choice_opr == 3:
#                 banker.search_customer()
#             elif choice_opr == 4:
#                 banker.view_all_customer()
#             elif choice_opr == 5:
#                 banker.total_amounts()
#             elif choice_opr == 6:
#                 banker.delete_customer()
#             elif choice_opr == 7:
#                 opr_Status = False
#             else:
#                 print("Invalid choice.")
#         except ValueError:
#             print("Please enter a valid number.")

# def customer_menu():
#     opr_Status = True
#     while opr_Status:
#         customer_Menu = """ 
#         Welcome to Customer App:

#                 Operations menu:
#                 Press:
#                 1) Withdraw money
#                 2) Deposit money
#                 3) View balance
#                 4) Back to main menu
#         """
#         print(customer_Menu)
#         try:
#             choice_Cust = int(input("Enter your choice: "))
#             if choice_Cust == 1:
#                 customer.withdraw()
#             elif choice_Cust == 2:
#                 customer.deposit()
#             elif choice_Cust == 3:
#                 customer.view_balance()
#             elif choice_Cust == 4:
#                 opr_Status = False
#             else:
#                 print("Invalid input.")
#         except ValueError:
#             print("Please enter a valid number.")

# status = True
# while status:
#     print("Welcome to Python BANK MANAGEMENT SYSTEM.")
#     print("\nSelect your role:")
#     role_menu = """
#         1) Banker
#         2) Customer
#         3) Exit
#     """
#     print(role_menu)
#     try:
#         role = int(input("Enter your role: "))
#         if role == 1:
#             banker_menu()
#         elif role == 2:
#             customer_menu()
#         elif role == 3:
#             print("Exiting... Thank you for using our bank system.")
#             status = False
#         else:
#             print("Invalid input. Try again.")
#     except ValueError:
#         print("Please enter a valid number.")