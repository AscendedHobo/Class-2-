import mysql.connector
from SQL_Settings import connectSQL     # my module for connect to SQL DB


mydb = connectSQL()

print(mydb)