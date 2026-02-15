

# CONNECT With SQL DATABASE :

import mysql.connector as a
password = input("DATABASE PASSWORD:")
con = a.connect(host="localhost", user="root", password='2005')
c = con.cursor()
# CREATE New Database IF DOES NOT EXIST :
c.execute("create database if not exists Book_Stall")
if con.is_connected():
    print("\n")
    print("    ___________________________________________________\n    ---------------------------------------------------")
    # SELECT DATABASE IF EXIST :
c.execute("use Book_Stall")

# CREATE New Table IF DOES NOT EXIST :

# ---------------------------------------------------------------------

# Structure Of Books Table:
c.execute("""create table if no2t exists BOOKS (B_Name varchar(50),
            B_Author varchar(50), CostPrice integer,
             SellPrice integer,Date varchar(20))""")

# ---------------------------------------------------------------------

# Structure Of Customers Table:
c.execute("""create table if not exists CUSTOMERS (C_Name varchar(20),
        Book varchar(25),Payment int,
         Date varchar(20),C_Phone varchar(50))""")

# ---------------------------------------------------------------------

# Structure Of Bills Table:
c.execute("""create table if not exists BILLS (Detail varchar(20),
         Cost int,GST int,Sum int,Date varchar(20))""")

# ---------------------------------------------------------------------

# Structure Of Workers Table:
c.execute("""create table if not exists WORKERS(W_Name varchar(100),
        Work varchar(20),W_Salary varchar(50))""")

# ---------------------------------------------------------------------


# SYSTEM PASSWORD LOGIN :
def signin():
    print("    >>>>>>>>>> WELCOME TO KHATIMA BOOK STALL <<<<<<<<<<")
    print("    ___________________________________________________\n    ---------------------------------------------------")
    print("\n")
    print("---------------------------")
    p = input("Are You Interested To Visit\n---------------------------\n(y/n)? :")
    if p == "y":
        options()
    else:
        signin()

# PROJECT WORKING OPTIONS


def options():
    print("\n")
    print("""                ----------------------------------------
                           KHATIMA BOOK STALL             
                ----------------------------------------
                1. Add Book          5. Display Books
                2. Sell Book         6. Display Payments
                3. Add Bill          7. Display Bills
                4. Add Wroker        8. Display Workers
                ________________________________________
                ----------------------------------------
                
    """)
    choice = input("SELECT OPTION:")
    while True:
        if choice == '1':
            AddBook()
        elif choice == '2':
            SellBook()
        elif choice == '3':
            AddBill()
        elif choice == '4':
            AddWorker()
        elif choice == '5':
            DisplayBooks()
        elif choice == '6':
            DisplayPayments()
        elif choice == '7':
            DisplayBills()
        elif choice == '8':
            DisplayWorkers()
        elif choice == '0':
            Exit()
       # If Wrong Value is Enter:
        else:
            print("Enter Again:")
            options()

# ADD BOOK :


def AddBook():
    n = input("B_Name:")
    a = input("B_Author:")
    c = int(input("Cost Price:"))
    s = int(input("Selling Price:"))
    d = input("Date:")
    data = (n, a, c, s, d)
    sql = 'insert into BOOKS values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully...")
    options()

# SELL BOOK :


def SellBook():
    n = input("C_Name:")
    b = input("Book:")
    py = int(input("Payment:"))
    d = input("Date:")
    ph = input("C_Phone:")
    data = (n, b, py, d, ph)
    sql = 'insert into CUSTOMERS values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully...")
    options()

# ADD BILL :


def AddBill():
    dt = input("Detail:")
    c = int(input("Cost:"))
    g = int(input("GST:"))
    s = int(input("Sum:"))
    d = input("Date:")
    data = (dt, c, g, s, d)
    sql = 'insert into BILLS values(%s,%s,%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully...")
    options()

# ADD WORKER :


def AddWorker():
    n = input("W_Name:")
    w = input("Work:")
    s = input("W_Salary:")
    data = (n, w, s)
    sql = 'insert into WORKERS values(%s,%s,%s)'
    c = con.cursor()
    c.execute(sql, data)
    con.commit()
    print("Data Inserted Successfully...")
    options()

# DISPLAY BOOKS :


def DisplayBooks():
    sql = 'select*from BOOKS'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("Name:", i[0], '|', "Author:", i[1], '|',
              "Cost:", i[2], '|', "Buy:", i[3], '|', "Date:", i[4])
        print("-----------------------------------------------------------------------")
    options()

# DISPLAY PAYMENTS :


def DisplayPayments():
    sql = 'select*from CUSTOMERS'

    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("Name:", i[0], '|', "Book:", i[1], '|', "Payment:",
              i[2], '|', "Date:", i[3], '|', "Phone:", i[4])
        print("------------------------------------------------------------------------")
    options()

# DISPLAY BILLS :


def DisplayBills():
    sql = 'select*from BILLS'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("Name:", i[0], '|', "Cost:", i[1], '|', "Tax:",
              i[2], '|', "Total", i[3], '|', "Date:", i[4])
        print("------------------------------------------------------------------------")
    options()

# DISPLAY WORKERS :


def DisplayWorkers():
    sql = 'select*from WORKERS'
    c = con.cursor()
    c.execute(sql)
    d = c.fetchall()
    for i in d:
        print("Name:", i[0], '|', "Work:", i[1], '|', "Salary:", i[2],)
        print("---------------------------------------------------")
    options()


signin()
