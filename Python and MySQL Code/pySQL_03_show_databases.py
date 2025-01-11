import mysql.connector
from SQL_Settings import connectSQL     # my module for connect to SQL DB

mydb = connectSQL()

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
