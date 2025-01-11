import mysql.connector
from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()

mycursor = mydb.cursor()

# alter the table, add new ID filed
mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")
