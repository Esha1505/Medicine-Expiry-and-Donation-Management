import json
import sys
from datetime import datetime, time, date


class Admin_Medicine_management:
    # ----------------------- Initiate all the variables -----------------------------------
    def add_med(self, med_id, med_name, batch_no, qty, price, mfg_date, exp_date, donar_comp):
        self.med_id = med_id
        self.med_name = med_name
        self.batch_no = batch_no
        self.qty = qty
        self.price = price
        self.mfg_date = mfg_date
        self.exp_date = exp_date
        self.donar_comp = donar_comp

        print(self.med_id)
    # ----------------------------------------------------------------------------------------

    # ------------------ Add Medicine Details in medicine.json file --------------------------
    def add_record(self):
        # ------- Add all the medicine detials in record dictionary -------------
        records = {
            "ID" : self.med_id, 
            "Name" : self.med_name, 
            "Batch" : self.batch_no, 
            "Quantity" : self.qty, 
            "Price" : self.price, 
            "Mfg Date" : self.mfg_date.strftime("%d-%m-%Y"), 
            "Exp Date" : self.exp_date.strftime("%d-%m-%Y"), 
            "Donar Company" : self.donar_comp
            }
        # -------------------------------------------------------------------------

        try:
            with open("medicine.json", "r") as f: # ----> read medicine.json file. 
                data = json.load(f) # --------> load all the existing records into 'data' variable. 

        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []

        for i in data:
            if i['ID'] == self.med_id:   # ---------> check is ID is already available
                if i['Name'] == self.med_name: # -------> check name
                    if i['Exp Date'] == self.exp_date.strftime("%d-%m-%Y"): # -------> check date
                        i['Quantity'] += self.qty   # --------> if id, name and date match then just add exp date in existing record instead adding completely duplicate record.  
                        with open("medicine.json", "w") as f:  # ------> write medicine.json file
                            json.dump(data, f, indent=2)
                        print("\nMedicne already found into the stock!")
                        print("Records added in the existing records")
                    return
            elif i['ID'] == self.med_id: # ------------> no medicine with same ID will recorded
                print("---------------------------------")
                print("Medicine ID already Available!!!")
                print("---------------------------------")
                return
            else:
                pass
        

        # -------------------- if ID, name does not match then add new record --------------------------
        data.append(records)
        with open("medicine.json", "w") as f:
            json.dump(data, f, indent=2)
            print("------------------------------")
            print("Record Added Successfully!!!")
            print("------------------------------")
        # -----------------------------------------------------------------------------------------------


    # ------------------------- View all the Medicine Records Available in the Stock ------------------------------
    def view_med(self):
        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)
            
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        if not data:
            print("No Records Found !!!")
        else:
        # --------------------- Print Details on Output Screen ---------------------------
            print(f"{'No':<4}{'ID':<10}{'Name':<20}{'Batch':<10}{'Qty':<10}{'Price':<10}")
            print("-" * 60)
        for i, item in enumerate(data, start=1):
            print(f"{i:<4}{item['ID']:<10}{item['Name']:<20}{item['Batch']:<10}{item['Quantity']:<10}{item["Price"]:<10}")
        # --------------------------------------------------------------------------------------

    # --------------------------- Search a single medicine available in the stock ------------------------------------
    def search_med(self, search):
        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)
            
            # search = input("Enter Name and ID of the medicine: ")
            found = False


            for i in data:
                if i["ID"].upper() == search.upper():  # ------------> Search Medicine with its ID 
                    print("\n Medicine Detail:")
                    print("-" * 100)
                    print(f"{'ID':<5}{'Name':<15}{'Batch_No':<10}{'Qty':<10}{'Price':<10}{'Mfg_date':<15}{'Exp_date':<15}{'Donar':<15}")
                    print("-" * 100)
                    print(f"{i['ID']:<5}{i['Name']:<15}{i['Batch']:<10}{i['Quantity']:<10}{i['Price']:<10}{i['Mfg Date']:<15}{i['Exp Date']:<15}{i['Donar Company']:<15}")
                    print("-" * 100)

                    found = True
                    break

                elif i['Name'].upper() == search.upper(): # -------------> Search Medicine with its Name 
                    print("\n Medicine Detail:")
                    print("-" * 45)
                    print(f"{'ID':<5}{'Name':<15}{'Batch_No':<10}{'Qty':<10}{'Price':<10}{'Mfg_date':<15}{'Exp_date':<15}{'Donar':<15}")
                    print("-" * 100)
                    print(f"{i['ID']:<5}{i['Name']:<15}{i['Batch']:<10}{i['Quantity']:<10}{i['Price']:<10}{i['Mfg Date']:<15}{i['Exp Date']:<15}{i['Donar Company']:<15}")
                    print("-" * 100)

                    found = True
                    break

            if found is False: # ---------------> if ID or Name not match
                print("No medicine found")
                    
        except FileNotFoundError:
            print("\n File not Found!!!! \n")
    
    # ---------------------------------------------------------------------------------------------------------------

    # ------------------------------- Check the Expiry Details of all the availabl medicine -------------------------
    def check_exp(self):
        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)
            
            if not data:
                print("No Medicine Record fOUND!")
                return
            
            today = date.today()
                
            data.sort(key=lambda i: datetime.strptime(i['Exp Date'], "%d-%m-%Y")) # ----------> sort medicine exp date 
            
            print("-" * 100)
            print("List of Medicine Expiry Details")
            print("-" * 100)

            print(f"{'ID':<8}{'Name':<20}{'Batch':<10}{'Quantity':<10}{'Price':<10}{'Exp Date':<15}{'Days Left':<10}{'Status':<15}")
            print("-" * 100)

            for i in data:

                exp_date = datetime.strptime(i['Exp Date'], "%d-%m-%Y").date()

                days_left = (exp_date - today).days
                status = ""

                if days_left == 0:
                    status = "EXPIRED TODAY"
                elif days_left < 0:
                    status = "EXPIRED"
                elif 0 < days_left <= 30:
                    status = "EXPIRE IN A MONTH"
                else:
                    status = "SAFE"

                print(
                    f"{i['ID']:<8}"
                    f"{i['Name']:<20}"
                    f"{i['Batch']:<10}"
                    f"{i['Quantity']:<10}"
                    f"{i['Price']:<10}"
                    f"{i['Exp Date']:<15}"
                    f"{days_left:<10}"
                    f"{status:<15}"
                )

        
        except FileNotFoundError:
            print("File is not available!!!!")
    # ---------------------------------------------------------------------------------

    # -------------------- Donate Medicine Function ------------------------------------
    def donate_med(self, medicine, m_qty, donate_to):
        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            print("File not found error. ")
        except json.JSONDecodeError:
            print("JSON decoder error")

        found = False

        for item in data:
            if item['Name'].upper() == medicine.upper():
                found = True
                if item['Quantity'] >= m_qty:
                    item['Quantity'] -= m_qty
                    print("Medicine deducted from the med stock!")
                    print("Sucessfully Donated the Medicines.")

                else:
                    print("Insufficient Medicine in the stock")
                    while True:
                        # ----------------- If you enter quantity greater then dtock available --------------------------
                        yes_no = input(f"Do you want to continue with less then {item['Quantity']} medicines (yes/no)")
                        if yes_no == "yes":
                            amt = int(input("Enter amount of medicine you want now: "))
                            item['Quantity'] -= amt
                            print("Medicine deducted from the medicine stock!")
                        else:
                            print("Donation Cancelled!!!")
                            break
                        # ------------------------------------------------------------------------------------------------

                # ---------- If the quantity of the medicine become zero then 'delete' the record and release its space --------- 
                if item['Quantity'] == 0:
                    data.remove(item)
                #-----------------------------------------------------------------------------------------------------------------
        if not found: # --------> if medicine not found. 
            print("Medicine not found")
        

        try:
            with open("medicine.json", "w") as f: # --------> update record in medicine.json file. 
                json.dump(data, f, indent=2)
        except FileNotFoundError:
            print("File not found!!!")
        except json.JSONDecodeError:
            print("JSON file decoder error")

        for item in data:
            if item['Name'].upper() == medicine.upper() or item['ID'].upper() == medicine.upper():
                record = {
                    "ID": item['ID'],
                    "Name": item['Name'],
                    "Quantity": m_qty,
                    "Mfg Date": item['Mfg Date'],
                    "Exp Date": item['Exp Date']
                }

        try:
            with open("donation.json", "r") as f: # ----------> update reocrd in donation.json file. 
                donate_data = json.load(f)
        except FileNotFoundError:
            donate_data = []
        except json.JSONDecodeError:
            donate_data = []

        donate_data.append(record)
        with open("donation.json", "w") as f:
            json.dump(donate_data, f, indent=2)
    # -----------------------------------------------------------------------------------------------------------------
        
    # ---------------------------- Request for medicine function ---------------------------------------------
    def req_med(self, medicine, m_qty, to_company):
        self.medicine = medicine
        self.m_qty = m_qty
        self.to_company = to_company

        # ------- Store all the medicine details in record dictionary------------
        record = {
            "Name": self.medicine,
            "Quantity": self.m_qty,
            "Requested Company": self.to_company
        }
        # -----------------------------------------------------------------------

        try:
            with open("request_med.json", "r") as f: # ----------> read request_med.json file. 
                req_data = json.load(f)  # --------> load existing records
        except FileNotFoundError:
            req_data = []
        except json.JSONDecodeError:
            req_data = []

        req_data.append(record) 
        with open("request_med.json", "w") as f: # ----------> write into request_med.json file. 
            json.dump(req_data, f, indent=2)
            print("Medicine request Placed.")

    # ------------------------------------------------------------------------------------------------------------

    # ----------------------------------View all the Medicine which are requested --------------------------------
    def view_req(self):
        try:
            with open("request_med.json", "r") as f:
                data = json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

        if not data:
            print("Data not available!!!")
        
        else:
            print("-" * 50)
            print("View Requested Medicines")
            print("-" * 50)
            print(f"{"NO":<4}{"Name":<10}{"Quantity":<15}{"Company":<15}")
            print("-" * 50)
            for i, item in enumerate(data, start=1):
                print(f"{i:<4}{item['Name']:<20}{item['Quantity']:<15}{item['Requested Company']:<15}")
            print("-" * 50)
    # ------------------------------------------------------------------------------------------------------
     
    # ------------------------------ Check Stock Medicines -------------------------------------------------
    def stock(self):
        try:
            with open("medicine.json", "r") as f:
                med_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found and json decoder error!")

        print("-" * 80)
        print(f"{'Name':<20}{'Quantity':<10}{'Price':<10}{'Exp Date':<20}")
        print("-" * 80)
        
        found = False
        for i in med_data:
            try:
                if i['Quantity'] <= 100:
                    found = True
                    print(
                        f"{i['Name']:<20}"
                        f"{i['Quantity']:<10}"
                        f"{i['Price']:<10}"
                        f"{i['Exp Date']:<20}"
                    )
            except KeyError as e:
                print(f"Missing key {e} in this record: {i}")

        if not found:
            print("Stock is full with Medicines.")

    # ------------------------------------- Ship Orders to the customers -------------------------------------
    def shipping(self):
        medicine = input("Enter the medicine name: ")
        customer = input("Enter the Paitent name: ")

        try:
            with open("medicine.json", "r") as f:
                med_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("file not found or json decoder error!")

        found = False
        while True:
            for i in med_data:  # ---------------> Check is medicine is in stock or not
                if i['Name'].lower() == medicine.lower():
                    found = True
            if not found:
                print("Medicne not available in stock!")
                break

            try:
                with open("orders.json", "r") as f:
                    order_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("file not found or json file decoder error!")

            found = False
            qty = 0
            for i in order_data:
                if i['Medicine Name'].lower() == medicine.lower():
                    qty = i['Quantity']
                    order_data.remove(i) # -------------> remove medicine data from orders.json file
                    found = True
                try:
                    with open("orders.json", "w") as f:
                        json.dump(order_data, f, indent=2)
                except (FileNotFoundError, json.JSONDecodeError):
                    print("File not found or json decoder error!")

            if not found:
                print("Medicine never ordered!")
                print("2")
                break

            try:
                with open("medicine.json", "r") as f:
                    med_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("file not found or json decoder error!")

            for i in med_data:
                if i['Name'].lower() == medicine.lower():
                    i['Quantity'] -= qty  # -----------> update the quantity of medicines after shipping medicines
                    

                try:
                    with open("medicine.json", "w") as f:
                        json.dump(med_data, f, indent=2)
                except (FileNotFoundError, json.JSONDecodeError):
                    print("FIle not found or json decoder error!")

            try:
                with open("history.json", "r") as f:
                    his_data = json.load(f)
            except (FileNotFoundError, json.JSONDecodeError):
                print("file not found or json decoder error!")

            for i in his_data:
                if i['Medicine Name'] == medicine:
                    i['Status'] == "Order Completed"
            
            try:
                with open("history.json", "w") as f:
                    json.dump(his_data, f, indent=2)
                    print("Medicine Shipped Successfully.")
                    break
            except (FileNotFoundError, json.JSONDecodeError):
                    print("FIle not found or json decoder error!")

        

    def sale(self, medicine, m_qty, sale_to, payment):
        try:
            with open("sale.json", "r") as f:
                sale_data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            sale_data = []


        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)
        except (FileNotFoundError, json.JSONDecodeError):
            print("File not found or json decoder error!")

        found = False

        for item in data:
            if item['Name'].upper() == medicine.upper():
                found = True
                if item['Quantity'] >= m_qty:
                    item['Quantity'] -= m_qty
                    print("Medicine deducted from the med stock!")

                else:
                    print("Insufficient Medicine in the stock")
                    while True:
                        # ----------------- If you enter quantity greater then stock available --------------------------
                        yes_no = input(f"Do you want to continue with less then {item['Quantity']} medicines (yes/no)")
                        if yes_no == "yes":
                            amt = int(input("Enter amount of medicine you want now: "))
                            item['Quantity'] -= amt
                            print("Medicine deducted from the medicine stock!")
                        else:
                            print("Donation Cancelled!!!")
                            break
                        # ------------------------------------------------------------------------------------------------

                # ---------- If the quantity of the medicine become zero then 'delete' the record and release its space --------- 
                if item['Quantity'] == 0:
                    data.remove(item)
                #-----------------------------------------------------------------------------------------------------------------
        if not found: # --------> if medicine not found. 
            print("Medicine not found")
        
        try:
            with open("medicine.json", "w") as f: # --------> update record in medicine.json file. 
                json.dump(data, f, indent=2)
        except FileNotFoundError:
            print("File not found!!!")
        except json.JSONDecodeError:
            print("JSON file decoder error")

        record = {
            "Medicine Name": medicine,
            "Quantity": m_qty,
            "Sale To": sale_to,
            "Payment": payment
        }

        sale_data.append(record)
        try:
            with open("sale.json", "w") as f:
                json.dump(sale_data, f, indent=2)
        except (FileNotFoundError, josn.JSONDecodeError):
            print("File not foun dor json ")

        print("Medicine sold successfully!")

        


            



    # -------------------------------------------------------------------------------------------------------------

# ------------------------- Class Closed ------------------------------------------

med = Admin_Medicine_management()  # -------> Object

def admin_menu():
    print("-----Medicine Expiry and Donation Mangement!-----")
    exit_loop = ""
    while True:
        print("\n======================================")
        print("1. Add Medicine")
        print("2. View Medicine")
        print("3. Search Medicine")
        print("4. Check Expiry")
        print("5. Donate/Sale Medicine")
        print("6. Request Medicine")
        print("7. View Request")
        print("8. Ship Customers Order")
        print("9. Check Stock of Medicines")
        print("10. Exit")
        print("======================================\n")


        try:

            choice = int(input("Enter Your Choice: "))

            if choice == 1: 
                # Add Medicines
                try:
                    ID = input("Enter Medicine ID: ")
                    name = input("Enter Medicine Name: ")
                    batch_no = input("Enter Batch Number: ")
                    while True:
                        try:
                            qty = int(input("Enter Quantity of Medicines: "))

                            if qty <= 0:
                                print("Enter Quantity in numberic form. ")
                            else:
                                break
                
                        except ValueError:
                            print("Enter the data in numberic. ")

                    while True:
                        try:
                            price = int(input("Enter price of the single medicine: "))

                            if price <= 0:
                                print("Enter Price in numberic form.")
                            else:
                                break
                
                        except ValueError:
                            print("Enter the data in numberic. ")

                    while True:
                        try:
                            mfg_date = input("Enter Manufacturing Date(DD-MM-YYYY): ")
                            exp_date = input("Enter Expiry Date(DD-MM-YYYY): ")

                            # ---------------- Formate Dates ---------------------

                            mfg_date = datetime.strptime(mfg_date, "%d-%m-%Y")
                            exp_date = datetime.strptime(exp_date, "%d-%m-%Y")

                            # ------------------------------------------------------

                            if mfg_date.date():
                                break
                
                        except ValueError:
                            print("Enter Date properly accordin to the format (DD-MM-YYYY)")

                    donar_comp = input("Enter name of Donar Company: ")        

                    if not ID or not name or not batch_no or not qty or not price or not mfg_date or not exp_date:
                        print("One of the field is empty")   

                except ValueError:
                    print("Please Enter the Information correct!!!")  


                med.add_med(ID, name, batch_no, qty, price, mfg_date, exp_date, donar_comp) # ------> function call with parameters
                med.add_record() # ----------> function call
        
        
            elif choice == 2:
                # View Medicines
                med.view_med()  # -------> function call. 

                

            elif choice == 3:
                # Search Medicines
                search = input("Enter Name and ID of the medicine: ")
                med.search_med(search)  # --------> function call. 

            elif choice == 4:
                # Check Expiry Date
                med.check_exp() # ---------> function call

            elif choice == 5:
                # donate medicine 
                while True:
                    sale = input("What you want to do Donate/Sale Medicine: ").lower()
                    if sale == "donate" or sale == "sale":
                        break
                    else:
                        print("Enter input correctly!")
                if sale == "donate":
                    medicine = input("Enter the name of medicine/ID of the medicine: ")
                    while True:
                        try:
                            m_qty = int(input("Enter the Quantity of the medicine: "))

                            if m_qty > 0:
                                break
                            else:
                                print("Quantity cannot be less the 0.")

                        except ValueError:
                            print("Enter the quantity of medicine in numeric only. ")

                    donate_to = input("Enter the name of person whom donating the medicine: ")

                    med.donate_med(medicine, m_qty, donate_to) # ---------> function call. 
                else:
                    medicine = input("Enter the name of medicine/ID of the medicine: ")
                    while True:
                        try:
                            m_qty = int(input("Enter the Quantity of the medicine: "))

                            if m_qty > 0:
                                break
                            else:
                                print("Quantity cannot be less the 0.")

                        except ValueError:
                            print("Enter the quantity of medicine in numeric only. ")

                    sale_to = input("Enter the name of person whom saling medicine: ")
                    while True:
                        payment = input("Enter mode of payment (cash/online): ").lower()
                        if payment == "cash" or payment == "online":
                            break
                        else:
                            print("Enter the input correctly!")
                    med.sale(medicine, m_qty, sale_to, payment)


            elif choice == 6:
                # request or order medicines
                medicine = input("Enter the name of medicine you want to request: ")
                while True:
                    try:
                        m_qty = int(input("Enter the Quantity of the medicine: "))
                        if m_qty < 0:
                            print("Enter Quantity Greater than 0.")
                        else:
                            break
                    except ValueError:
                        print("Enter number in numberic formate.")
                to_company = input("ENter the name of company you want to request for medicine: ")
                med.req_med(medicine, m_qty, to_company) # ------------> function call. 

            elif choice == 7:
                # View medicine Request
                med.view_req() # -----------> function call. 

            elif choice == 8:
                # Ship Order of the customer
                med.shipping()

            elif choice == 9:
                # check stocks
                med.stock()

            elif choice == 10:
                print("-" * 50)
                print("Thank You for using this software.........")
                print("-" * 50)
                sys.exit()

            else:
                print("Choose number between (1-8) only:")
     
        except ValueError:
            print("Enter option in numbers between(1-8)")
  

# ---------------------------------------------------------------------------------------------------------

def login():
    username = ["esha", "shani"]
    password = ["esha12345", "shani12345"]
    while True:
        enter_username = input("Enter User Name: ").lower()
        enter_password = input("Enter password: ").lower()
    
        if enter_username not in username:
            print("Invalid Username!!!")
        elif enter_password not in password:
            print("Invalid Password!!!")
        else:
            print("Successfully LogIn!!!")
            admin_menu()