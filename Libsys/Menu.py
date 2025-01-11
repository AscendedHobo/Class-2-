import tkinter as tk
import subprocess
import os

# Define the path to the directory where the modules are located
BASE_PATH = r"C:\Users\alanw\Documents\GitHub\Class\Libsys"

def open_members():
    """Open the member management module."""
    subprocess.Popen(['python', os.path.join(BASE_PATH, 'members.py')])

def open_books():
    """Open the book management module."""
    subprocess.Popen(['python', os.path.join(BASE_PATH, 'books.py')])

def open_loans():
    """Open the loan management module."""
    subprocess.Popen(['python', os.path.join(BASE_PATH, 'loans.py')])

def main_window():
    """Create the main GUI window for the library system."""
    root = tk.Tk()
    root.title("Small Local Library")

    # Title Label
    tk.Label(root, text="Small Local Library", font=("Arial", 16, "bold")).grid(row=0, column=0, columnspan=2, pady=10)

    # Buttons for Management Sections
    tk.Button(root, text="Member Management", width=20, command=open_members).grid(row=1, column=0, pady=5)
    tk.Button(root, text="Book Management", width=20, command=open_books).grid(row=2, column=0, pady=5)
    tk.Button(root, text="Loan Management", width=20, command=open_loans).grid(row=3, column=0, pady=5)

    root.mainloop()

main_window()
