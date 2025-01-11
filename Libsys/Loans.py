import mysql.connector
import tkinter as tk
from tkinter import messagebox
from main import connect_to_database
####################################################################
# Function to Create a Loan
def create_loan(memberid, bookid):
    """Create a new loan and update the book's status."""
    mydb = connect_to_database()
    mycursor = mydb.cursor()

    # Check if the book is already on loan
    check_book_query = """
        SELECT Status FROM Books
        WHERE BookID = %s;
    """
    mycursor.execute(check_book_query, (bookid,))
    book_status = mycursor.fetchone()

    if not book_status or book_status[0] != 'Available':
        print("This book is already on loan or does not exist.")
        messagebox.showerror("Error", "This book is not available for borrowing.")
        mydb.close()
        return

    # Insert the loan into the Loans table
    loan_insert_query = """
        INSERT INTO Loans (MemberID, BookID, BorrowDate, DueDate, ReturnDate)
        VALUES (%s, %s, CURDATE(), DATE_ADD(CURDATE(), INTERVAL 14 DAY), NULL);
    """
    loan_values = (memberid, bookid)
    mycursor.execute(loan_insert_query, loan_values)

    # Update the book's status
    update_book_query = """
        UPDATE Books
        SET Status = 'On Loan'
        WHERE BookID = %s;
    """
    mycursor.execute(update_book_query, (bookid,))

    mydb.commit()
    print(f"Loan created for MemberID {memberid} and BookID {bookid}.")
    mydb.close()

# Function to Return a Book
def return_book(bookid):
    """Return a book, update the loan, and check for overdue status."""
    mydb = connect_to_database()
    mycursor = mydb.cursor()

    # Find the active loan for the book
    loan_query = """
        SELECT LoanID, DueDate FROM Loans
        WHERE BookID = %s AND ReturnDate IS NULL;
    """
    mycursor.execute(loan_query, (bookid,))
    loan = mycursor.fetchone()

    if not loan:
        print("No active loan found for this book.")
        mydb.close()
        return

    loan_id, due_date = loan

    # Check for null DueDate
    if due_date is None:
        print("Loan record is missing a DueDate.")
        messagebox.showerror("Error", "The loan record does not have a valid DueDate.")
        mydb.close()
        return

    # Update the loan with the return date
    return_query = """
        UPDATE Loans
        SET ReturnDate = CURDATE()
        WHERE LoanID = %s;
    """
    mycursor.execute(return_query, (loan_id,))

    # Retrieve the current date
    current_date_query = "SELECT CURDATE();"
    mycursor.execute(current_date_query)
    current_date = mycursor.fetchone()[0]

    # Check for overdue status
    overdue = due_date < current_date
    if overdue:
        messagebox.showinfo("Notice", "This book is being returned late.")

    # Update the book's status
    update_book_query = """
        UPDATE Books
        SET Status = 'Available'
        WHERE BookID = %s;
    """
    mycursor.execute(update_book_query, (bookid,))

    mydb.commit()
    print(f"BookID {bookid} returned successfully.")
    mydb.close()




# Tkinter GUI for Borrowing and Returning Books
def loan_management_gui():
    """Create a GUI for managing book loans and returns."""

    def show_borrow_fields():
        # Show fields for borrowing
        memberid_label.grid(row=2, column=0)
        memberid_entry.grid(row=2, column=1)
        bookid_label.grid(row=3, column=0)
        bookid_entry.grid(row=3, column=1)
        action_button.config(text="Borrow Book", command=borrow_book)

    def show_return_fields():
        # Show fields for returning
        memberid_label.grid_remove()
        memberid_entry.grid_remove()
        bookid_label.grid(row=2, column=0)
        bookid_entry.grid(row=2, column=1)
        action_button.config(text="Return Book", command=return_book_gui)

    def borrow_book():
        memberid = memberid_entry.get()
        bookid = bookid_entry.get()

        try:
            create_loan(int(memberid), int(bookid))
            messagebox.showinfo("Success", "Loan created successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")

    def return_book_gui():
        bookid = bookid_entry.get()

        try:
            return_book(int(bookid))
            messagebox.showinfo("Success", "Book returned successfully!")
        except Exception as e:
            messagebox.showerror("Error", f"An error occurred: {e}")


    # GUI Window
    root = tk.Tk()
    root.title("Loan Management")

    # Buttons to select action
    tk.Label(root, text="Choose Action:").grid(row=0, column=0, columnspan=2)
    tk.Button(root, text="Borrow Book", command=show_borrow_fields).grid(row=1, column=0)
    tk.Button(root, text="Return Book", command=show_return_fields).grid(row=1, column=1)

    # Common Fields
    memberid_label = tk.Label(root, text="Member ID")
    memberid_entry = tk.Entry(root)

    bookid_label = tk.Label(root, text="Book ID")
    bookid_entry = tk.Entry(root)

    action_button = tk.Button(root, text="", command=None)
    action_button.grid(row=4, column=0, columnspan=2)

    root.mainloop()

# Run the GUI
loan_management_gui()
