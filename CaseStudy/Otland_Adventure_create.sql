/*
    Campbell Alexander
    Outland Adventures
    11JUL2021
    Professor Sampson
*/
""" import statements """
import mysql.connector as mysql
from mysql.connector import errorcode

""" database config object """

#Creating a Function to create the database
def database_create():
    db = mysql.connect(
        user = "Outdoor_Adventure_user",
        password = "MySQL8IsGreat!",
        host = "127.0.0.1",
    )

    mycursor = db.cursor()

    mycursor.execute("CREATE DATABASE Outdoor_Adventure")
    mycursor.close()


""" database config object """

#Creating a Function read a .sql file that establishes the empty tables for the database
def database_structure():
    db = mysql.connect(
        user = "Outdoor_Adventure_user",
        password = "MySQL8IsGreat!",
        host = "127.0.0.1",
        database = "Outdoor_Adventure",
    )

    mycursor = db.cursor()

    with open('C:\\Users\\alexd\\Desktop\\Outland_Adventure\\Outland_Adventure_Tablescreate.sql') as f:
        mycursor.execute(f.read(), multi=True)


database_create()
database_structure()

