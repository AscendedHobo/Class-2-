from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()

mycursor = mydb.cursor()

sql = "SELECT * FROM customers ORDER BY name"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)