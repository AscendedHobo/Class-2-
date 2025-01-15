import mysql.connector
import tkinter as tk
from tkinter import messagebox
from main import connect_to_database

# Function to Add a Book to the Database
def add_book(title, author):
    """Add a new book to the Books table."""
    # Step 1: Connect to the database
    mydb = connect_to_database()
    mycursor = mydb.cursor()

    # Step 2: Insert the book into the Books table
    insert_book_query = """
        INSERT INTO Books (Title, Author)   
        VALUES (%s, %s)
    """
    book_values = (title, author)
    mycursor.execute(insert_book_query, book_values)

    # Commit the transaction
    mydb.commit()
    print(f"Book '{title}' by '{author}' added successfully.")

    # Close the connection
    mydb.close()

# Function to Remove a Book from the Database
def remove_book(book_id):
    """Remove a book from the Books table."""
    # Step 1: Connect to the database
    mydb = connect_to_database()
    mycursor = mydb.cursor()

    # Step 2: Delete the book from the Books table
    delete_book_query = """
        DELETE FROM Books WHERE BookID = %s
    """
    mycursor.execute(delete_book_query, (book_id,))

    # Commit the transaction
    mydb.commit()
    print(f"Book with ID '{book_id}' removed successfully.")

    # Close the connection
    mydb.close()

# Tkinter GUI for Adding and Removing Books
def manage_books_gui():
    """Create a Tkinter GUI for managing books."""

    def add_book_gui():
        title = title_entry.get()
        author = author_entry.get()

        try:
            # Add the book to the database
            add_book(title, author)
            messagebox.showinfo("Success", "Book added successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def remove_book_gui():
        book_id = book_id_entry.get()

        try:
            # Remove the book from the database
            remove_book(int(book_id))
            messagebox.showinfo("Success", "Book removed successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    # GUI Window
    root = tk.Tk()
    root.title("Manage Books")

    # Add Book Section
    tk.Label(root, text="Add Book").grid(row=0, column=0, columnspan=2)

    tk.Label(root, text="Title").grid(row=1, column=0)
    title_entry = tk.Entry(root)
    title_entry.grid(row=1, column=1)

    tk.Label(root, text="Author").grid(row=2, column=0)
    author_entry = tk.Entry(root)
    author_entry.grid(row=2, column=1)

    add_button = tk.Button(root, text="Add Book", command=add_book_gui)
    add_button.grid(row=3, column=0, columnspan=2)

    # Remove Book Section

    tk.Label(root, text="Book ID").grid(row=5, column=0)
    book_id_entry = tk.Entry(root)
    book_id_entry.grid(row=5, column=1)

    remove_button = tk.Button(root, text="Remove Book", command=remove_book_gui)
    remove_button.grid(row=6, column=0, columnspan=2)

    root.mainloop()

# Run the GUI
manage_books_gui()
