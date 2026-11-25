import json
import admin
import paitent
print("-"*100)
print("~Medicine Expiry and Donation Management~")
print("Welcome to the Project!!!!")
print("-"*100)
print("\n")

def main_fun():
    while True:
        print("Please Log in as:")
        print("-"*50)
        print(" 1. Admin.")
        print(" 2. Patient")
        
        try:
            choice = int(input("Enter your choice: "))
            if choice == 1:
                admin.login()
            elif choice == 2:
                paitent.login_register()
            else:
                print("Please enter 1 or 2")
        except ValueError:
            print("Enter value in numberic form only...")

main_fun() 