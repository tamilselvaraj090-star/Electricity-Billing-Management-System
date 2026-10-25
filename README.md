# Electricity Billing Management System

## 1. Project Overview
The Electricity Billing Management System is a Core Python project developed to manage customer details, calculate electricity bills, maintain bill history, and generate billing reports.

## 2. Technologies Used
- Python
- JSON for data storage
- CSV for exporting customer details
- File Handling
- VS Code

## 3. Project Objectives
- Store and manage electricity customer information.
- Calculate electricity bills based on units consumed.
- Save bill history and generate text receipts.
- Track paid and unpaid bills.
- Generate billing reports.
- Export customer details to a CSV file.

## 4. Main Features
1. Add Customer
2. View Customers
3. Generate Electricity Bill
4. Search Customer
5. Delete Customer
6. Update Customer
7. View Bill History
8. View Paid / Unpaid Bills
9. Billing Report
10. Export Customer Details to CSV
11. Save Bill Receipt as a Text File
12. Search Bill History

## 5. Electricity Bill Calculation
- Up to 100 units: ₹2 per unit
- 101–200 units: ₹2 for the first 100 units and ₹3 for each additional unit
- Above 200 units: ₹2 for the first 100 units, ₹3 for the next 100 units, and ₹5 for each additional unit

Example: For 150 units, the bill amount is ₹350.

## 6. Files Used
- `electricity_billing.py` — Main Python program
- `customers.json` — Customer information
- `bill_history.json` — Generated bill history
- `customers_report.csv` — Exported customer details
- `receipt_*.txt` — Generated bill receipts

## 7. How to Run
1. Install Python.
2. Open the project folder in VS Code.
3. Open the terminal.
4. Run:

   `python electricity_billing.py`

5. Select an option from the menu.

## 8. Conclusion
This project demonstrates Python fundamentals, functions, loops, conditional statements, exception handling, JSON and CSV file handling. It provides a simple way to manage electricity customers and their billing records.

