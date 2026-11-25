import json
from datetime import datetime, date, time
import random
import string
import sys

class Paitent_Medicine_management:

    def record(self, name):
        self.name = name
    
    # --------------- Add Medicine Order details in orders.json file --------------
    def order(self, name):
        cart =[]
        # ------ Get data ------------
        while True:
            order_id = int(datetime.now().timestamp())
            medicine = input("Enter medidicne name: ")
            try:
                qty = int(input("Enter medicine Quantity: "))
                if qty <= 0:
                    print("Enter quantity greater than 0.")
                    continue

            except ValueError:
                print("Enter Quantity in numberic form only!")
        
            try:
                with open("medicine.json", "r") as f:
                    data = json.load(f)
            except FileNotFoundError:
                print("File not found!!")
            
            # ---------- Check medicine name and quantity of medicine ---------

            found = False
            for i in data:
                if i['Name'].lower() == medicine.lower():
                    found =  True
            if not found:
                print("Medicine not available!")
                return

            for i in data:
                if i['Name'].lower() == medicine.lower():
                    found =  True
                    if i['Quantity'] < qty:
                        print("Inefficient Stock of medicine")
                    else:
                        print(f"---Cost of one medicine: {i['Price']}---")
                        i['Quantity'] -= qty
                        price = qty * i['Price']
            
            

        
            order_date = datetime.now().strftime("%d-%m-%Y %H:%M:%S")
            address = input("Enter delivery address: ")

            record = {
                "Order ID": order_id,
                "Customer Name": name,
                "Medicine Name": medicine,
                "Quantity": qty,
                "Price": price,
                "Order Date": order_date,
                "Address": address,
                "Status": "Order Placed"
            }

            # ------------- Add order details in orders.json file --------------
            try:
                with open("orders.json", "r") as f:
                    order_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("File not found or decoder error!")
                
            order_data.append(record)
            cart.append(record)
            try:
                with open("orders.json", "w") as f:
                    json.dump(order_data, f, indent=2)
            except (FileNotFoundError, json.JSONDecodeError):
                print("File not found or decoder error!")
            
            # ----------------------------------------------------------------
            
            # --------------- Insert data into history file. ---------------
            
            try:
                with open("history.json", "r") as f:
                    order_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("File not found or decoder error!")
                order_data = []
            order_data.append(record)

            try:
                with open("history.json", "w") as f:
                    json.dump(order_data, f, indent=2)
            except (FileNotFoundError, json.JSONDecodeError):
                print("File not found or decoder error!")
            
            # -----------------------------------------------------------------

            add = input("Do you want to add more medicines (y/n): ")
            if add == "y":
                pass
            elif add == "n":
                print("Order Placed Successfully!!!")
                break
            else:
                print("enter y/n only.")
        
        # --------------- Print Order Details on Console/Output screen ------------------

        print("========== Order Details ==========")
        print(f"{'ID':<15}{'Customer_Name':<20}{'Medicine_Name':<20}{'Quantity':<15}{'Price':<10}{'Order_Date':<30}{'Address':<25}{'Status':<10}")
        print("=" * 150)
        total_bill = 0
        for i in cart:
            print(
                f"{i['Order ID']:<15}"
                f"{i['Customer Name']:<20}"
                f"{i['Medicine Name']:<20}"
                f"{i['Quantity']:<15}"
                f"{i['Price']:<10}"
                f"{i['Order Date']:<30}"
                f"{i['Address']:<25}"
                f"{i['Status']:<20}"
            )
            total_bill += i['Price']
        print("=" * 150)
        print(f"Total Bill of medicines is: {total_bill}")
        print("\n")

        # ------------------------------------------------------------------------------------

    def cancel_order(self):
        medicine = input("Enter the name of medicine: ")
        # ------------------delelting recordes from orders.json file. -------------------
        try:
            with open("orders.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("file not found!!")
        found = False
        for i in data:
            if i['Medicine Name'].lower() == medicine.lower():
                quantity = i['Quantity']
                data.remove(i)
                found = True

        if not found:
            print("File not found in the cart")

        try:
            with open("orders.json", "w") as f:
                json.dump(data, f, indent=2)
        except (FileNotFoundError):
            print("file not found or decorder error")
        # --------------------------------------------------------------------------------

        # ------------------delelting recordes from history.json file. -------------------
        try:
            with open("history.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("file not found!!")
        found = False
        for i in data:
            if i['Medicine Name'].lower() == medicine.lower():
                quantity = i['Quantity']
                data.remove(i)
                found = True

        if not found:
            print("File not found in the cart")

        try:
            with open("history.json", "w") as f:
                json.dump(data, f, indent=2)
        except (FileNotFoundError):
            print("file not found or decorder error")
        # ------------------------------------------------------------------------------------

        # -------------------Updating records form medicine file. -----------------------------

        try:
            with open("medicine.json", "r") as f:
                main_data = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            print("File not found or decoder erroe!")

        found = False
        for i in main_data:
            if i['Name'].lower() == medicine.lower():
                i['Quantity'] += quantity
                found = True
                
        if not found:
            print("Medicine not found!")

        try:
            with open("medicine.json", "w") as f:
                json.dump(main_data, f, indent=2)
        except FileNotFoundError:
            print("file not found!")

        print("Medicine Removed Successfully.")


    # ----------------------- View all the Medicines which have been ordered --------------------------
    def view_cart(self):
        try:
            with open("orders.json", "r") as f: # -----------> read file with existing records
                order_data = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            print("File not found or JSON decoder Error!")
            return
        if not order_data:
            print("Cart is emplty!")
        
        found = False
        print("--------- Medicines into the Cart -------------")
        print("-" * 50)
        print(f"{'ID':<15}{'Medicine Name':<20}{'Quantity':<10}{'Price':<10}{'Address':<30}")
        print("-" * 80)
        for i in order_data:
            found = True
            if i['Customer Name'].lower() == self.name.lower():
                print(
                    f"{i['Order ID']:<15}"
                    f"{i['Medicine Name']:<20}"
                    f"{i['Quantity']:<10}"
                    f"{i['Price']:<10}"
                    f"{i['Address']:<30}"
                )
        if not found:
            print("Cart is Empty!")

    # -------------------------------------------------------------------------------------------------

    # ------------------------------ View History of all the medicine ordered ------------------------------
    def view_history(self):
        try:
            with open("history.json", "r") as f:
                his_data = json.load(f)
        except(FileNotFoundError, json.JSONDecodeError):
            print("File not found or decoder error ")
            return
        print(f"--------------- History ----------------------")
        print("-" * 100)
        print(f"{"Order ID":<15}{"Medicine Name":<15}{"Quantity":<10}{"Price":<10}{"Order Date":<20}{"Address:<20"}")
        print("-" * 100)
        for i in his_data:
            if i['Customer Name'].lower() == self.name.lower():
                print(
                    f"{i['Order ID']:<15}"
                    f"{i['Medicine Name']:<15}"
                    f"{i['Quantity']:<10}"
                    f"{i['Price']:<10}"
                    f"{i['Order Date']:<20}"
                    f"{i['Address']:<20}"
                    f"{i['Status']:<20}"
            )
    # ------------------------------------------------------------------------------------------------------
            
# -------------------- Class Closed --------------------------------------

med = Paitent_Medicine_management()     # ------> Object 

def paitent_menu(current_user):
    while True:
        print("-"*50)
        print("1. Order Medicine.")
        print("2. Cancel Medicine Order.")
        print("3. View Ordered Medicines.")
        print("4. View Purchase History.")
        print("5. Exit")
        print("-"*50)

        cust_name = current_user  # -----> this is use to auto detect username while adding order detail as we have logged in 
        med.record(cust_name)

        choice = int(input("Enter your Choice(1-5): "))
        try:
            # -----------------------------------------------
            if choice == 1:
                # Order Medicine
                while True:
                    print("-" * 50)
                    print("1. View Medicnes.")
                    print("2. Search Medicine.")
                    print("3. Directly Order Medicine.")
                    print("-" * 50)
                    try:
                        c = int(input("Enter your choice: "))
                        if c == 1:
                            with open("medicine.json", "r") as f:
                                view_med_data = json.load(f)
                            
                            print("-" * 100)
                            print(f"{"ID":<8}{"Name":<20}{"Price":<10}{"Exp Date":<10}")
                            print("-" * 100)
                            for i in view_med_data:
                                print(
                                    f"{i['ID']:<8}"
                                    f"{i['Name']:<20}"
                                    f"{i['Price']:<10}"
                                    f"{i['Exp Date']:<10}"
                                )
                            print("-" * 100)
                            print("\n")
                            break
                                
                        elif c == 2:
                            with open("medicine.json", "r") as f:
                                search_med_data = json.load(f)
                            search_med = input("Enter medicine name to search: ")
                            found = False
                            print("-" * 50)
                            print(f"{"ID":<8}{"Name":<20}{"Price":<10}{"Exp Date":<10}")
                            print("-" * 50)
                            for i in search_med_data:
                                if i['Name'].upper() == search_med.upper():
                                    found = True
                                    print(
                                        f"{i['ID']:<8}"
                                        f"{i['Name']:<20}"
                                        f"{i['Price']:<10}"
                                        f"{i['Exp Date']:<10}"
                                    )
                            print("-" * 50)

                            if not found:
                                print("-" * 50)
                                print("No medicine found.")
                                print("-" * 100)
                            print("\n")
                            break
                        


                        elif c== 3:
                            break
                        else:
                            print("Enter number between 1 to 3 only.")
                    except ValueError:
                        print("Ente your choice in numberic form only.")
                cust_name = current_user  # -----> this is use to auto detect username while adding order detail as we have logged in 
                med.order(cust_name)
            # -----------------------------------------------

            # ------------------------------------------------
            elif choice == 2:
                # Cancel Medicine Order 
                med.cancel_order()
            # -------------------------------------------------

            # -------------------------------------------------
            elif choice == 3:
                # View Cart
                med.view_cart()
            # -------------------------------------------------

            # -------------------------------------------------
            elif choice == 4:
                # View Purchase History
                med.view_history()
            # -----------------------------------------------------
            elif choice ==5:
                # Exit
                print("-" * 50)
                print("Thank You for using this software.........")
                print("-" * 50)
                sys.exit()
            # -----------------------------------------------------

            else:
                print("Enter numbers between (1-5) only.")
        except ValueError:
            print("\n Enter your choice itno numberic form only!!!\n")

# ------------------------ Login Function ----------------------------------------
def login():
    while True:
        user_name = input("Enter your username: ")
        password = input("Enter password: ")

        chapcha_len = 4
        characters = string.ascii_lowercase + string.digits
        capcha = "".join(random.choices(characters, k=chapcha_len )).upper()
        print("Check if You are not a Robot")
        print(f"Enter the exact capcha below: {capcha}")
        user_capcha = input("Enter Capcha: ").upper()

        if user_capcha.upper() != capcha.upper():
            print("Capcha didnt match \n Try again")
            break

        try:
            with open("users.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found")
            data = []

        for i in data:
            if user_name.lower() == i['First_name'].lower():
                if password == i['Password']:
                    print("Successfully Login!")
                    paitent_menu(user_name)
                    
        print("Incorrect username or password! \n Try again")
        break
# ---------------------------------------------------------------------------------

# ------------------------------ Registration Function ----------------------------
def registration():
    user_name = input("Enter your First Name: ")
    last_name = input("Enter your Last Name: ")
    password = input("Enter password: ")
    while True:
        try:
            age = int(input("Enter your Age: "))
            if age > 0:
                break
        except ValueError:
            print("Enter age in numberic form")
    while True:
        gender = input("Enter your gender as ('Male','Female','Other'): ").strip().lower()
        gender_list = ["male", "female", "other"]
        if gender in gender_list:
            break
            
    while True:
        try:
            phone_no = int(input("Enter phone number: "))
            phone_num = len(str(phone_no))
            if phone_num == 10:
                break
            else:
                print("Enter 10 digit phone number only!")
        except ValueError:
            print("Enter phone number in numeric form only")

    address = input("Enter your address: ")

    record = {
                "First_name" : user_name,
                "Last_name" : last_name,
                "Password" : password,
                "Age" : age,
                "Gender" : gender,
                "Phone_no" : phone_no,
                "Address" : address
            }

    try:
        with open("users.json", "r") as f:
            data = json.load(f)
            print("12345")
    except FileNotFoundError:
        print("File not found errror!")
        return []
    except json.JSONDecodeError:
        print("Json file not found error")
        return []

    found = False
    for i in data:
        if i['Phone_no'] == phone_no:
            found = True
            break
                
    if found == True:
        print("Already registered with the same phone number!")
    else:
        data.append(record)
        with open("users.json", "w") as f:
            json.dump(data, f, indent=2)
            print("Record Added successfully!")
            # user_name(first_name)

    paitent_menu(user_name)                

# ------------------------------------------------------------------------------------


def login_register():
    while True:
        try:
            print("1. Log IN")
            print("2. Register")
            print("3. Back")
            choice = int(input("Enter your choice: "))

            if choice == 1:
                # Log IN 
                login()

            elif choice == 2:
                # Register
                registration()

            elif choice == 3:
                break

            else:
                print("Enter number between 1 and 3")

        except ValueError:
            print("Enter input into numberic form only!!!")


