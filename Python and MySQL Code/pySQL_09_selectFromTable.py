from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()    # using my module
mycursor = mydb.cursor()

mycursor.execute("SELECT * FROM customers")

myresult = mycursor.fetchall()

for x in myresult:
  print(x)