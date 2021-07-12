
### Campbell Alexander
### Outland Adventures
###11JUL2021
###Professor Sampson

import mysql.connector as mysql
from mysql.connector import errorcode
db = mysql.connect(
        user = "Outdoor_Adventure_user",
        password = "MySQL8IsGreat!",
        host = "127.0.0.1",
    )
mycursor = db.cursor()
def location():
    sql = "INSERT INTO location (location_id) VALUES (%s)"
    val = [
        (1),
        (2),
        (3),
    ]
    mycursor.executemany(sql, val)
    db.commit()

def equiptment():
    sql = "INSERT INTO equiptment (equiptment_id, equiptment_name, equiptment_sales) VALUES (%s,%s,%s)"
    val = [
        (111, 'Bed_roll', 50),
        (212, 'Climbing_harness', 80),
        (323, 'hygiene_kit', 20),
        (434, 'camera', 15),
    ]
    mycursor.executemany(sql, val)
    db.commit()

def bookings():
    sql = "INSERT INTO bookings (customer_id, customer_name, total_customer, trip_id) VALUES (%s,%s,%s,%s)"
    val = [
    (100021,'Jane Doe', 2, 18),
    (122231,'John Dane', 3, 18),
    ]
    mycursor.executemany(sql, val)
    db.commit()

def acquisition_date():
    sql = "INSERT INTO acquisition_date (equiptment_id, equiptment_name, equiptment_cost, equiptment_acquired) VALUES (%s,%S,%s,%S)"
    val = [
        (111, 'Bed_roll', 20, 2017),
        (212, 'Climbing_harness', 99, 2017),
        (323, 'hygiene_kit', 35), 2020,
        (434, 'camera', 28), 2011,
    ]
    mycursor.executemany(sql, val)
    #Commiting the changes to the table
    db.commit()

def print_location():
    mycursor.execute("SELECT LOCATION_ID FROM location")
    print("\n -- DISPLAYING LOCATION ID --")
    location_info =mycursor.fetchall()
    for loc in location_info:
        print("Location ID: {}".format(loc[0]))

def print_equiptment():
    mycursor.execute("SELECT equiptment_id, equiptment_name, equiptment_sales FROM equiptment")
    print("\n -- DISPLAYING Equiptment info--")
    equiptment_info =mycursor.fetchall()
    for equi in equiptment_info:
        print("Equiptment ID: {}, equipment name: {}, Equiptment Sales ".format(equi[0], equi[1],equi[2]))

def print_bookings():
    mycursor.execute("SELECT customer_id, customer_name, total_customer, trip_id FROM bookings")
    print("\n -- DISPLAYING Booking Info--")
    bookings_info =mycursor.fetchall()
    for book in bookings:
        print("Customer ID: {}, Customer name: {}, Number of Customers: {}, Trip ID: {} ".format(book[0], book[1],book[2], book[3]))

def print_acquisition_date():
    mycursor.execute("SELECT equiptment_id, equiptment_name, equiptment_cost, equiptment_acquired FROM acquisition_date")
    print("\n -- DISPLAYING Equiptment Acquisition Info--")
    acquisition_info =mycursor.fetchall()
    for acq in bookings:
        print("Equiptment ID: {}, Equiptment name: {}, Equiptment cost: {}, Trip ID: {} ".format(acq[0], acq[1],acq[2], acq[3]))



