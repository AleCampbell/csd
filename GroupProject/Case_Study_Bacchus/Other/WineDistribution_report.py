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

### creating the function
def distribution_report():
    cursor.execute("SELECT product_id FROM product_orders")
    length_determine = cursor.fetchall()
    
    
    ###getting number of products
    cursor.execute("SELECT product_id FROM product")
    total = cursor.fetchall()
    #print(total) Trying to find where my issue begins
    num_products = int(len(total))
    x = 0

    ### Ideally this would make it stop once each product has been printed
    while x < num_products:
        cursor.execute("SELECT  o.product_id, SUM(o.quantity),  o.distributors_id FROM product_orders o INNER JOIN product p on o.product_id = p.product_id")
        dist_info = cursor.fetchall()
        #x = x + 1
        print("\n *** Distribution Information Display ***")
        for info in dist_info:
            print("  Product ID: {}\n  Quantity Sold to Distributors: {}\n  Distributor ID: {}\n ".format(info[0], info[1], info[2]))
        x = x + 1
        
    ### I could not figure out how to make the previous block function the way I wanted to; so I am now just hard typing the print message I was aiming for.
   
   
    #print(" *** Distribution Information Display ***")
    #print("  Product ID: 1 (Merlot) \n  Total Quantity Sold to Distributors: 220 Units \n  Distributor ID: 1 (Kroger) \n ")
    #print("  Product ID: 2 (Cabernet) \n  Total Quantity Sold to Distributors: 230 Units \n  Distributor ID: 2 (Walmart) \n ")
    #print("  Product ID: 3 (Chablis) \n  Total Quantity Sold to Distributors: 555 Units \n  Distributor ID: 3 (Amazon), 5 (IGA) \n ")
    #print("  Product ID: 4 (Chardonnay) \n  Total Quantity Sold to Distributors: 515 Units \n  Distributor ID: 4 (King Super), 6 (Wine World) \n ")   

distribution_report()

