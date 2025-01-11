from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()

mycursor = mydb.cursor()

mycursor.execute("SELECT name FROM customers")

myresult = mycursor.fetchone()

print(myresult)