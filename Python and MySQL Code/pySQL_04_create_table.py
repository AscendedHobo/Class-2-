import mysql.connector

from SQL_Settings import connectDB     # my module for connect to SQL DB


mydb = connectDB()

mycursor = mydb.cursor()

mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")
