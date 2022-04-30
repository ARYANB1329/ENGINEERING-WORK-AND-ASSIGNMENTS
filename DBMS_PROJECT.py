import mysql.connector

database = mysql.connector.connect(
    host='localhost',
    user='root',
    password='aryan12@',
    port='3306',
    database='LibraryData'
)
cursor1 = database.cursor()


def func():
    print("   ** Our STUDENT DATABASE provides the following options:  **   ")

    print("""
            (1) VIEW DETAILS
            (2) ADD DETAILS
            (3) VIEW MEMBERSHIP
            (4) ADD MEMBERSHIP
            (5) VIEW BOOKS
            (6) VIEW SUPPLIERS
            (7) ADD BOOKS
            (8) BORROW
            (9) TO READ
            (0) EXIT
                    """)

    print("  ..............  Select one from the above options  ..............  ")

    option = input("Enter Your Choice No.: ")

    if option == "1":
        viewdetails()
    elif option == "2":
        adddetails()
    elif option == "3":
        viewmembership()
    elif option == "4":
        addmembership()
    elif option == "5":
        viewbooks()
    elif option == "6":
        viewsuppliers()
    elif option == "7":
        addbooks()
    elif option == "8":
        borrow()
    elif option == "9":
        read()
    elif option == "0":
        endprogram()
    else:
        print("Try Again! Please, chose from the given options ")


def viewdetails():
    cursor1.execute('SELECT * FROM STUDENT')
    users = cursor1.fetchall()
    for user in users:
        print(user)
    return


def adddetails():
    print("")


def viewmembership():
    cursor1.execute('SELECT * FROM MEMBERSHIP')
    users = cursor1.fetchall()
    for user in users:
        print(user)
    return


def addmembership():
    print("")


def viewbooks():
    sqlcode = 'SELECT B.BOOK_ID,B.BOOK_NAME,B.AUTHOR,B.TYPE_CODE,T.TYPE_NAME FROM BOOKS B, BOOKTYPE T WHERE ' \
              'B.TYPE_CODE = T.BCODE ORDER BY B.BOOK_ID '
    cursor1.execute(sqlcode)
    users = cursor1.fetchall()
    for user in users:
        print(user)
    return


def viewsuppliers():
    cursor1.execute('SELECT * FROM SUPPLIER')
    users = cursor1.fetchall()
    for user in users:
        print(user)
    return


def addbooks():
    print("")


def borrow():
    print("")


def read():
    print("")


def endprogram():
    print(".....................   Thank You! ...................")
    print(" .....................   Closing The Application!   ..................")
    return


ID = input("Enter Login ID: ")
Password = input("Password: ")
if ID == 'DBMS_PROJ':
    if Password == 'admin12@':
        print("           WELCOME TO THE LIBRARY DATA MANAGEMENT SYSTEM          ")
        func()
    else:
        print("Please enter the correct password")
else:
    print("Please enter the correct LOGIN ID")
