import mysql.connector
import tkinter as tk
from tkinter import messagebox

# Database Connection Function
def connect_to_database():
    """Connect to the MySQL database and return the connection object."""
    mydb = mysql.connector.connect(
        host="192.168.1.150",
        port=3306,
        user="Alan Welch",
        password="warcraft91",
        database="HandCodedLibDB"
    )
    return mydb