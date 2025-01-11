import mysql.connector

mydb = mysql.connector.connect(
    host='KK-X1', 
    user='mysqluser',
    password='mysql')

print(mydb)

mycursor = mydb.cursor()

mycursor.execute("SHOW DATABASES")

for x in mycursor:
    print(x)
