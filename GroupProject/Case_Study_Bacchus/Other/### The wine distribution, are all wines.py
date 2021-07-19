### The wine distribution, are all wines selling as they thought? Is one wine not selling? Which distributor carries which wine

""" 
    Title: Wine_Distribution_report.py
    Group: Bravo
    Author: Campbell, Hinkle, Luna, Orozco, Upadhyaya
    Date: 15 July 2021
    Description: Pulling table data from MySQL database bacchus, 
"""

""" import statements """
import mysql.connector as mysql
from mysql.connector import errorcode


""" database config object """
db = mysql.connect(
    user = "bacchus_user",
    password = "MySQL8IsGreat!",
    host = "127.0.0.1",
    database = "bacchus",
)


cursor = db.cursor()

#Creating empty list variable for later use
distribution_listing = []

#Creating function that will be called to print requested distribution data
def distribution_report():
    cursor.execute("SELECT product_id FROM product_orders")
    length_determine = cursor.fetchall()
    x = 0
    y = 0
    #Selecting all of the employee Ids to see how many employees there are
    cursor.execute("SELECT product_id FROM product")
    total = cursor.fetchall()
    num_products = int(len(total))

    while x < num_products:
        cursor.execute("SELECT o.product_id, o.quantity,  o.distributors_id FROM product_orders o INNER JOIN product p on o.product_id = p.product_id" + str(y))
        dist_info = cursor.fetchall()
        #distribution_listing.append([dist_info[0][0],dist_info[0][1],dist_info[0][2],dist_info[0][3]+dist_info[1][3]+dist_info[2][3]+dist_info[3][3]])
        print(dist_info)
        x = x + 1
        y = y + 1
        print("\n *** Distribution Information Display ***")
        

        #for prod in distribution_listing:
        #    print(" Product ID: {} \n Product Name: {}\n Quantity Ordered:  {}\n Distributor ID: {}\n ".format(prod[0], prod[1],prod[2], prod[3]))
        

distribution_report()
