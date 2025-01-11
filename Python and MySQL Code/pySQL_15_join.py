from SQL_Settings import connectDB     # my module for connect to SQL DB

mydb = connectDB()

mycursor = mydb.cursor()


sql = "SELECT * FROM users INNER JOIN products ON users.fav = products.id"

mycursor.execute(sql)

myresult = mycursor.fetchall()

for x in myresult:
  print(x)