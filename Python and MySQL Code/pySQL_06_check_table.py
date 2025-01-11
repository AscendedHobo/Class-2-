from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()

mycursor = mydb.cursor()

mycursor.execute("SHOW TABLES")

for x in mycursor:
  print(x)
