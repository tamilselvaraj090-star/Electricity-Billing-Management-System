
# customers = []

# def add_customer():
#     print("\n--- Add Customer ---")

#     customer_id = input("Enter Customer ID: ")
#     name = input("Enter Customer Name: ")
#     address = input("Enter Address: ")
#     units = int(input("Enter Electricity Units: "))

#     customer = {
#         "id": customer_id,
#         "name": name,
#         "address": address,
#         "units": units
#     }

#     customers.append(customer)
#     print("Customer added successfully!")


# def view_customers():
#     print("\n--- Customer Details ---")

#     if not customers:
#         print("No customer records found.")
#         return

#     for customer in customers:
#         print("------------------------")
#         print("Customer ID:", customer["id"])
#         print("Name:", customer["name"])
#         print("Address:", customer["address"])
#         print("Units:", customer["units"])


# def generate_bill():
#     customer_id = input("Enter Customer ID: ")

#     for customer in customers:
#         if customer["id"] == customer_id:
#             units = customer["units"]

#             if units <= 100:
#                 amount = units * 2
#             elif units <= 200:
#                 amount = 100 * 2 + (units - 100) * 3
#             else:
#                 amount = 100 * 2 + 100 * 3 + (units - 200) * 5

#             print("\n--- Electricity Bill ---")
#             print("Customer Name:", customer["name"])
#             print("Customer ID:", customer["id"])
#             print("Units Consumed:", units)
#             print("Total Bill Amount: Rs.", amount)
#             return

#     print("Customer not found!")


# while True:
#     print("\n===== Electricity Billing System =====")
#     print("1. Add Customer")
#     print("2. View Customers")
#     print("3. Generate Bill")
#     print("4. Exit")

#     choice = input("Enter your choice: ")

#     if choice == "1":
#         add_customer()
#     elif choice == "2":
#         view_customers()
#     elif choice == "3":
#         generate_bill()
#     elif choice == "4":
#         print("Thank you!")
#         break
#     else:
#         print("Invalid choice. Try again.")





# 



import json
import os
import time

FILE_NAME = "customers.json"


def load_customers():
    if os.path.exists(FILE_NAME):
        with open(FILE_NAME, "r") as file:
            return json.load(file)
    return []


def save_customers():
    with open(FILE_NAME, "w") as file:
        json.dump(customers, file, indent=4)


customers = load_customers()


BILL_FILE = "bill_history.json"


def save_bill_history(bill):
    if os.path.exists(BILL_FILE):
        with open(BILL_FILE, "r") as file:
            history = json.load(file)
    else:
        history = []

    history.append(bill)

    with open(BILL_FILE, "w") as file:
        json.dump(history, file, indent=4)



def add_customer():
    print("\n--- Add Customer ---")

    customer_id = input("Enter Customer ID: ")

    for customer in customers:
        if customer["id"] == customer_id:
            print("Customer ID already exists!")
            return

    name = input("Enter Customer Name: ")
    address = input("Enter Address: ")

    try:
        units = int(input("Enter Electricity Units: "))
        if units < 0:
            print("Units cannot be negative!")
            return
    except ValueError:
        print("Please enter valid units!")
        return

    customer = {
        "id": customer_id,
        "name": name,
        "address": address,
        "units": units
    }

    customers.append(customer)
    save_customers()

    print("Customer added and saved successfully!")


def view_customers():
    print("\n--- Customer Details ---")

    if not customers:
        print("No customer records found.")
        return

    for customer in customers:
        print("------------------------")
        print("Customer ID:", customer["id"])
        print("Name:", customer["name"])
        print("Address:", customer["address"])
        print("Units:", customer["units"])




def generate_bill():
    customer_id = input("Enter Customer ID: ")

    for customer in customers:
        if customer["id"] == customer_id:
            units = customer["units"]

            if units <= 100:
                amount = units * 2
            elif units <= 200:
                amount = 100 * 2 + (units - 100) * 3
            else:
                amount = 100 * 2 + 100 * 3 + (units - 200) * 5

            print("\n--- Electricity Bill ---")
            print("Customer Name:", customer["name"])
            print("Customer ID:", customer["id"])
            print("Units Consumed:", units)
            print("Total Bill Amount: Rs.", amount)

            
            payment_status = input("Payment Status (paid/unpaid): ").lower()

            if payment_status not in ["paid", "unpaid"]:
                print("Invalid payment status!")
                return


            bill = {
                "id": customer["id"],
                "name": customer["name"],
                "units": units,
                "amount": amount,
                "payment_status": payment_status
            }


            save_bill_history(bill)
            print("Bill history saved successfully!")

            import time
            bill_number = str(int(time.time()))

            receipt = f"""
            Payment Status: {payment_status}
================================
     ELECTRICITY BILL RECEIPT
================================
Bill Number   : {bill_number}
Customer ID   : {customer["id"]}
Customer Name : {customer["name"]}
Units Used    : {units}
Bill Amount   : Rs. {amount}
================================
Thank you!
================================
"""

            file_name = f"receipt_{bill_number}.txt"

            with open(file_name, "w") as file:
                file.write(receipt)

            print("Bill receipt saved as:", file_name)
            return

    print("Customer not found!")




def search_customer():
    customer_id = input("Enter Customer ID to search: ")

    for customer in customers:
        if customer["id"] == customer_id:
            print("\n--- Customer Found ---")
            print("Customer ID:", customer["id"])
            print("Name:", customer["name"])
            print("Address:", customer["address"])
            print("Units:", customer["units"])
            return

    print("Customer not found!")


    
def billing_report():
    print("\n===== Electricity Billing Report =====")

    total_customers = len(customers)
    total_units = 0
    total_amount = 0

    for customer in customers:
        total_units += customer["units"]

        units = customer["units"]

        if units <= 100:
            amount = units * 2
        elif units <= 200:
            amount = 100 * 2 + (units - 100) * 3
        else:
            amount = 100 * 2 + 100 * 3 + (units - 200) * 5

        total_amount += amount

    print("Total Customers:", total_customers)
    print("Total Units Consumed:", total_units)
    print("Total Bill Amount: Rs.", total_amount)




import csv

def export_customers_csv():
    if not customers:
        print("No customer records to export.")
        return

    with open("customers_report.csv", "w", newline="") as file:
        writer = csv.writer(file)

        writer.writerow([
            "Customer ID",
            "Name",
            "Address",
            "Units"
        ])

        for customer in customers:
            writer.writerow([
                customer["id"],
                customer["name"],
                customer["address"],
                customer["units"]
            ])

    print("Customer details exported to customers_report.csv")



def view_payment_status():
    if not os.path.exists(BILL_FILE):
        print("No bill history found.")
        return

    with open(BILL_FILE, "r") as file:
        history = json.load(file)

    status = input("Enter status (paid/unpaid): ").lower()

    if status not in ["paid", "unpaid"]:
        print("Invalid status!")
        return

    found = False

    print(f"\n--- {status.upper()} Bills ---")

    for bill in history:
        if bill.get("payment_status") == status:
            print("------------------------")
            print("Customer ID:", bill["id"])
            print("Customer Name:", bill["name"])
            print("Units:", bill["units"])
            print("Bill Amount: Rs.", bill["amount"])
            print("Payment Status:", bill["payment_status"])
            found = True

    if not found:
        print("No bills found for this status.")



def search_bill_history():
    if not os.path.exists(BILL_FILE):
        print("No bill history found.")
        return

    with open(BILL_FILE, "r") as file:
        history = json.load(file)

    customer_id = input("Enter Customer ID to search bills: ")
    found = False

    print("\n--- Customer Bill History ---")

    for bill in history:
        if bill["id"] == customer_id:
            print("------------------------")
            print("Customer ID:", bill["id"])
            print("Customer Name:", bill["name"])
            print("Units:", bill["units"])
            print("Bill Amount: Rs.", bill["amount"])
            print("Payment Status:",
                  bill.get("payment_status", "Not recorded"))
            found = True

    if not found:
        print("No bills found for this Customer ID.")



  
def view_bill_history():
    if not os.path.exists(BILL_FILE):
        print("No bill history found.")
        return

    with open(BILL_FILE, "r") as file:
        history = json.load(file)

    if not history:
        print("No bill history found.")
        return

    print("\n--- Bill History ---")

    for bill in history:
        print("------------------------")
        print("Customer ID:", bill["id"])
        print("Customer Name:", bill["name"])
        print("Units:", bill["units"])
        print("Bill Amount: Rs.", bill["amount"])




def update_customer():
    customer_id = input("Enter Customer ID to update: ")

    for customer in customers:
        if customer["id"] == customer_id:
            print("\n--- Update Customer ---")
            print("1. Update Name")
            print("2. Update Address")
            print("3. Update Units")

            choice = input("Enter your choice: ")

            if choice == "1":
                customer["name"] = input("Enter New Name: ")

            elif choice == "2":
                customer["address"] = input("Enter New Address: ")

            elif choice == "3":
                try:
                    units = int(input("Enter New Units: "))
                    if units < 0:
                        print("Units cannot be negative!")
                        return
                    customer["units"] = units
                except ValueError:
                    print("Please enter valid units!")
                    return

            else:
                print("Invalid choice!")
                return

            save_customers()
            print("Customer details updated successfully!")
            return

    print("Customer not found!")


def delete_customer():
    customer_id = input("Enter Customer ID to delete: ")

    for customer in customers:
        if customer["id"] == customer_id:
            print("Customer Name:", customer["name"])
            confirm = input("Are you sure you want to delete? (yes/no): ")

            if confirm.lower() == "yes":
                customers.remove(customer)
                save_customers()
                print("Customer deleted successfully!")
            else:
                print("Delete cancelled.")

            return

    print("Customer not found!")


while True:
    print("\n===== Electricity Billing System =====")
    print("1. Add Customer")
    print("2. View Customers")
    print("3. Generate Bill")
    print("4. Exit")
    print("5. Search Customer")
    print("6. Delete Customer")
    print("7. View Bill History")
    print("8. Update Customer")
    print("9. View Paid / Unpaid Bills")
    print("10. Billing Report")
    print("11. Export Customer Details to CSV")
    print("12. Search Bill History")

    choice = input("Enter your choice: ")

    if choice == "1":
        add_customer()
    elif choice == "2":
        view_customers()
    elif choice == "3":
        generate_bill()
    elif choice == "4":
        print("Thank you!")
        break
    elif choice == "5":
        search_customer()
    elif choice == "6":
        delete_customer()
    elif choice == "7":
        view_bill_history()
    elif choice == "8":
        update_customer()
    elif choice == "9":
        view_payment_status()
    elif choice == "10":
        billing_report()
    elif choice == "11":
        export_customers_csv()
    elif choice == "12":
        search_bill_history()
    else:
        print("Invalid choice. Try again!")
