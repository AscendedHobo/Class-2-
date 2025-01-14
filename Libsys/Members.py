import mysql.connector
import tkinter as tk
from tkinter import messagebox
from main import connect_to_database

# Function to Insert Member into Database
def insert_add_member_gui_to_db(first_name, last_name, DOB, PostCode, Email):
    """Insert a new member into the database."""
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = """
        INSERT INTO members (FirstName, LastName, DateOfBirth, PostCode, Email)
        VALUES (%s, %s, %s, %s, %s);
    """
    val = (first_name, last_name, DOB, PostCode, Email)
    mycursor.execute(sql, val)
    mydb.commit()
    mydb.close()

# Function to Remove Member from Database
def remove_member_from_db(member_id):
    """Remove a member from the database."""
    mydb = connect_to_database()
    mycursor = mydb.cursor()
    sql = """
        DELETE FROM members WHERE MemberID = %s;
    """
    mycursor.execute(sql, (member_id,))
    mydb.commit()
    mydb.close()



# Tkinter GUI for Adding or Removing Members
def manage_members_gui():
    """Create a Tkinter GUI for adding or removing members."""

    def add_member():
        first_name = first_name_entry.get()
        last_name = last_name_entry.get()
        DOB = DOB_entry.get()
        PostCode = PostCode_entry.get()
        Email = email_entry.get()

        try:
            insert_add_member_gui_to_db(first_name, last_name, DOB, PostCode, Email)
            messagebox.showinfo("Success", "Member added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def remove_member():
        member_id = member_id_entry.get()

        try:
            remove_member_from_db(int(member_id))
            messagebox.showinfo("Success", "Member removed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    root = tk.Tk()
    root.title("Manage Members")

    # Add Member Section
    tk.Label(root, text="Add Member").grid(row=0, column=0, columnspan=2)

    tk.Label(root, text="First Name").grid(row=1, column=0)
    first_name_entry = tk.Entry(root)
    first_name_entry.grid(row=1, column=1)

    tk.Label(root, text="Last Name").grid(row=2, column=0)
    last_name_entry = tk.Entry(root)
    last_name_entry.grid(row=2, column=1)

    tk.Label(root, text="Date of Birth (YYYY-MM-DD)").grid(row=3, column=0)
    DOB_entry = tk.Entry(root)
    DOB_entry.grid(row=3, column=1)

    tk.Label(root, text="Post Code").grid(row=4, column=0)
    PostCode_entry = tk.Entry(root)
    PostCode_entry.grid(row=4, column=1)

    tk.Label(root, text="Email").grid(row=5, column=0)
    email_entry = tk.Entry(root)
    email_entry.grid(row=5, column=1)

    add_button = tk.Button(root, text="Add Member", command=add_member)
    add_button.grid(row=6, column=0, columnspan=2)

    # Remove Member Section
    tk.Label(root, text="Remove Member").grid(row=7, column=0, columnspan=2)

    tk.Label(root, text="Member ID").grid(row=8, column=0)
    member_id_entry = tk.Entry(root)
    member_id_entry.grid(row=8, column=1)

    remove_button = tk.Button(root, text="Remove Member", command=remove_member)
    remove_button.grid(row=9, column=0, columnspan=2)

    root.mainloop()

# Run the GUI
manage_members_gui()
