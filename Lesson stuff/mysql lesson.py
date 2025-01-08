import mysql.connector

mydb = mysql.connector.connect(
    host='localhost',
    user='root',
    password='warcraft91',
  database= "testDB"
)

mycursor = mydb.cursor()
mycursor.execute("SELECT * FROM customers")
myresult = mycursor.fetchall()
for x in myresult:
    print(x)
###########################################################################################################################################################################
# mycursor = mydb.cursor()

# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")

# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"
# val = ("John", "Highway 21")
# mycursor.execute(sql, val)
# mydb.commit()
# print(mycursor.rowcount, "record inserted.")

###########################################################################################################################################################################

# mycursor = mydb.cursor()

# # SQL query to delete a record with id = 2
# # sql = "DELETE FROM customers WHERE id = 2"
# sql ="UPDATE customers SET address = 'Canyon 123' WHERE address = 'Valley 345'"

# mycursor.execute(sql)
# mydb.commit()

# # Print the number of records deleted
# print(mycursor.rowcount, "record(s) deleted")



###########################################################################################################################################################################
# mycursor = mydb.cursor()

# # SQL query for inserting data
# sql = "INSERT INTO customers (name, address) VALUES (%s, %s)"

# # Data to insert
# val = [
#     ('Peter', 'Lowstreet 4'),
#     ('Amy', 'Apple st 652'),
#     ('Hannah', 'Mountain 21'),
#     ('Michael', 'Valley 345'),
#     ('Sandy', 'Ocean blvd 2'),
#     ('Betty', 'Green Grass 1'),
#     ('Richard', 'Sky st 331'),
#     ('Susan', 'One way 98'),
#     ('Vicky', 'Yellow Garden 2'),
#     ('Ben', 'Park Lane 38'),
#     ('William', 'Central st 954'),
#     ('Chuck', 'Main Road 989'),
#     ('Viola', 'Sideway 1633')
# ]

# # Execute multiple insertions
# mycursor.executemany(sql, val)
# mydb.commit()

# # Confirmation message
# print(mycursor.rowcount, "records were inserted.")

###########################################################################################################################################################################

# # Creation template 
# mycursor = mydb.cursor()
# mycursor.execute("CREATE DATABASE TestDB")

###########################################################################################################################################################################

# Table creation
# mycursor = mydb.cursor()
# mycursor.execute("CREATE TABLE customers (name VARCHAR(255), address VARCHAR(255))")


###########################################################################################################################################################################

# mycursor.execute("ALTER TABLE customers ADD COLUMN id INT AUTO_INCREMENT PRIMARY KEY")


###########################################################################################################################################################################
# showing template 
# mycursor = mydb.cursor()
# mycursor.execute("SHOW customers")

# for x in mycursor:
#     print(x)

###########################################################################################################################################################################