import json
from datetime import datetime, time, date


class Medicine_management:
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


    def add_record(self):
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

        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)

        except FileNotFoundError:
            data = []
        except json.JSONDecodeError:
            data = []

        for i in data:
            if i['ID'] == self.med_id:
                print("---------------------------------")
                print("Medicine ID already Available!!!")
                print("---------------------------------")
                return
            elif i['Name'] == self.med_name:
                if i['Exp Date'] == self.exp_date.strftime("%d-%m-%Y"):
                    i['Quantity'] += self.qty
                    with open("medicine.json", "w") as f:
                        json.dump(data, f, indent=2)
                    print("\nMedicne already found into the stock!")
                    print("Records added in the existing records")
                    return
        


        data.append(records)
        with open("medicine.json", "w") as f:
            json.dump(data, f, indent=2)
            print("------------------------------")
            print("Record Added Successfully!!!")
            print("------------------------------")



    def view_med(self):
        try:
            with open("medicine.json", "r") as f:
                return json.load(f)
            
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []

    def search_med(self, search):
        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)
            
            # search = input("Enter Name and ID of the medicine: ")
            found = False


            for i in data:
                if i["ID"].upper() == search.upper():
                    print("\n Medicine Detail:")
                    print("-" * 100)
                    print(f"{'ID':<5}{'Name':<15}{'Batch_No':<10}{'Qty':<10}{'Price':<10}{'Mfg_date':<15}{'Exp_date':<15}{'Donar':<15}")
                    print("-" * 100)
                    print(f"{i['ID']:<5}{i['Name']:<15}{i['Batch']:<10}{i['Quantity']:<10}{i['Price']:<10}{i['Mfg Date']:<15}{i['Exp Date']:<15}{i['Donar Company']:<15}")
                    print("-" * 100)

                    found = True
                    break

                elif i['Name'].upper() == search.upper():
                    print("\n Medicine Detail:")
                    print("-" * 45)
                    print(f"{'ID':<5}{'Name':<15}{'Batch_No':<10}{'Qty':<10}{'Price':<10}{'Mfg_date':<15}{'Exp_date':<15}{'Donar':<15}")
                    print("-" * 100)
                    print(f"{i['ID']:<5}{i['Name']:<15}{i['Batch']:<10}{i['Quantity']:<10}{i['Price']:<10}{i['Mfg Date']:<15}{i['Exp Date']:<15}{i['Donar Company']:<15}")
                    print("-" * 100)

                    found = True
                    break
            if found is False:
                print("No medicine found")
                    
        except FileNotFoundError:
            print("\n File not Found!!!! \n")

    def check_exp(self):
        try:
            with open("medicine.json", "r") as f:
                data = json.load(f)
            
            if not data:
                print("No Medicine Record fOUND!")
                return
            
            today = date.today()
                
            data.sort(key=lambda i: datetime.strptime(i['Exp Date'], "%d-%m-%Y"))
            
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

                else:
                    print("Insufficient Medicine in the stock")
                    while True:
                        yes_no = input(f"Do you want to continue with less then {item['Quantity']} medicines (yes/no)")
                        if yes_no == "yes":
                            amt = int(input("Enter amount of medicine you want now: "))
                            item['Quantity'] -= amt
                            print("Medicine deducted from the medicine stock!")
                        else:
                            print("Donation Cancelled!!!")
                            break

                if item['Quantity'] == 0:
                    data.remove(item)
        if not found:
            print("Medicine not found")

        try:
            with open("medicine.json", "w") as f:
                json.dump(data, f, indent=2)
        except FileNotFoundError:
            print("File not found!!!")
        except json.JSONDecodeError:
            print("JSON file decoder error")

        record = {
            "ID": item['ID'],
            "Name": item['Name'],
            "Quantity": item['Quantity'],
            "Mfg Date": item['Mfg Date'],
            "Exp Date": item['Exp Date']
        }

        try:
            with open("donation.json", "r") as f:
                donate_data = json.load(f)
        except FileNotFoundError:
            donate_data = []
        except json.JSONDecodeError:
            donate_data = []

        donate_data.append(record)
        with open("donation.json", "w") as f:
            json.dump(donate_data, f, indent=2)
        

    def req_med(self, medicine, m_qty, to_company):
        self.medicine = medicine
        self.m_qty = m_qty
        self.to_company = to_company

        record = {
            "Name": self.medicine,
            "Quantity": self.m_qty,
            "Requested Company": self.to_company
        }
        try:
            with open("request_med.json", "r") as f:
                req_data = json.load(f)
        except FileNotFoundError:
            req_data = []
        except json.JSONDecodeError:
            req_data = []

        req_data.append(record)
        with open("request_med.json", "w") as f:
            json.dump(req_data, f, indent=2)

    def view_req(self):
        try:
            with open("request_med.json", "r") as f:
                return json.load(f)
        except FileNotFoundError:
            return []
        except json.JSONDecodeError:
            return []



med = Medicine_management()
print("-----Medicine Expiry and Donation Mangement!-----")
while True:
    print("\n======================================")
    print("1. Add Medicine")
    print("2. View Medicine")
    print("3. Search Medicine")
    print("4. Check Expiry")
    print("5. Donate Medicine")
    print("6. Request Medicine")
    print("7. View Request")
    print("8. Exit")
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

                        mfg_date = datetime.strptime(mfg_date, "%d-%m-%Y")
                        exp_date = datetime.strptime(exp_date, "%d-%m-%Y")

                        if mfg_date.date():
                            break
                
                    except ValueError:
                        print("Enter Date properly accordin to the format (DD-MM-YYYY)")

                donar_comp = input("Enter name of Donar Company: ")        

                if not ID or not name or not batch_no or not qty or not price or not mfg_date or not exp_date:
                    print("One of the field is empty")   

            except ValueError:
                print("Please Enter the Information correct!!!")  


            med.add_med(ID, name, batch_no, qty, price, mfg_date, exp_date, donar_comp)
            med.add_record()
        
        
        elif choice == 2:
            # View Medicines
            data = med.view_med()

            if not data:
                print("No Records Found !!!")
            else:
                print(f"{'No':<4}{'ID':<10}{'Name':<20}{'Batch':<10}{'Qty':<10}{'Price':<10}")
                print("-" * 60)
                for i, item in enumerate(data, start=1):
                    print(f"{i:<4}{item['ID']:<10}{item['Name']:<20}{item['Batch']:<10}{item['Quantity']:<10}{item["Price"]:<10}")

        elif choice == 3:
            # Search Medicines
            search = input("Enter Name and ID of the medicine: ")
            med.search_med(search)

        elif choice == 4:
            # Check Expiry Date
            med.check_exp()

        elif choice == 5:
            # donate medicine 
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

            donate_to = input("Enter the name fo persone to donate medicine: ")

            med.donate_med(medicine, m_qty, donate_to)

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
            med.req_med(medicine, m_qty, to_company)

        elif choice == 7:
            # View medicine Request
            data = med.view_req()

            if not data:
                print("Data not available!!!")
        
            else:
                print("-" * 50)
                print("View Requested Medicines")
                print("-" * 50)
                print(f"{"NO":<4}{"Name":<10}{"Quantity":<15}{"Company":<15}")
                print("-" * 50)
                for i, item in enumerate(data, start=1):
                    print(f"{i:<4}{item['Name']:<10}{item['Quantity']:<15}{item['Requested Company']:<15}")
                    print("-" * 50)


        elif choice == 8:
            print("-" * 50)
            print("Thank You for using this software.........")
            print("-" * 50)
            break

        else:
            print("Choose number between (1-8) only:")
     
    except ValueError:
        print("Enter option in numbers between(1-8)")