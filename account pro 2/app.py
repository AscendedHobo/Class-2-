from flask import Flask, render_template, request, redirect, url_for, flash
import mysql.connector
from flask_bcrypt import Bcrypt
from flask_login import LoginManager, UserMixin, login_user, logout_user, login_required, current_user

app = Flask(__name__)
app.secret_key = "your_secret_key"  # Change this to something secure

bcrypt = Bcrypt(app)
login_manager = LoginManager()
login_manager.init_app(app)
login_manager.login_view = "login"

# Database configuration
db_config = {
    'host': '127.0.0.1',
    'user': 'root',
    'password': 'warcraft91',
    'database': 'accounting'
}

# Function to get a database connection
def get_db_connection():
    return mysql.connector.connect(**db_config)

# User Model
class User(UserMixin):
    def __init__(self, id, name, email, role, password):
        self.id = id
        self.name = name
        self.email = email
        self.role = role
        self.password = password

# Load user for Flask-Login
@login_manager.user_loader
def load_user(user_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT * FROM User WHERE UserID = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    if user:
        return User(user["UserID"], user["Name"], user["Email"], user["Role"], user["Password"])
    return None

#homepage Route
@app.route("/")
def home():
    return render_template("home.html")


# Login Route
@app.route("/login", methods=["GET", "POST"])
def login():
    if request.method == "POST":
        email = request.form["email"]
        password = request.form["password"]

        conn = get_db_connection()
        cursor = conn.cursor(dictionary=True)
        cursor.execute("SELECT * FROM User WHERE Email = %s", (email,))
        user = cursor.fetchone()
        cursor.close()
        conn.close()

        if user and bcrypt.check_password_hash(user["Password"], password):
            user_obj = User(user["UserID"], user["Name"], user["Email"], user["Role"], user["Password"])
            login_user(user_obj)
            return redirect(url_for("dashboard"))
    
    return render_template("login.html")


# fetch users
@login_required
@app.route("/users", methods=["GET"])
def list_users():
    if current_user.role != "Admin":
        flash("You don't have permission to view users.", "danger")
        return redirect(url_for("dashboard"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    cursor.execute("SELECT UserID, Name, Email, Role FROM User")
    users = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("users.html", users=users)


# add users 
@login_required
@app.route("/add_user", methods=["GET", "POST"])
def add_user():
    if current_user.role != "Admin":
        flash("You don't have permission to add users.", "danger")
        return redirect(url_for("dashboard"))

    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        role = request.form["role"]
        password = bcrypt.generate_password_hash(request.form["password"]).decode("utf-8")

        conn = get_db_connection()
        cursor = conn.cursor()
        cursor.execute("INSERT INTO User (Name, Email, Role, Password) VALUES (%s, %s, %s, %s)", 
                       (name, email, role, password))
        conn.commit()
        cursor.close()
        conn.close()

        flash("User added successfully!", "success")
        return redirect(url_for("list_users"))

    return render_template("add_user.html")

#edit users
@login_required
@app.route("/edit_user/<int:user_id>", methods=["GET", "POST"])
def edit_user(user_id):
    if current_user.role != "Admin":
        flash("You don't have permission to edit users.", "danger")
        return redirect(url_for("dashboard"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)
    
    if request.method == "POST":
        name = request.form["name"]
        email = request.form["email"]
        role = request.form["role"]
        
        cursor.execute("UPDATE User SET Name = %s, Email = %s, Role = %s WHERE UserID = %s",
                       (name, email, role, user_id))
        conn.commit()
        cursor.close()
        conn.close()

        flash("User updated successfully!", "success")
        return redirect(url_for("list_users"))

    cursor.execute("SELECT * FROM User WHERE UserID = %s", (user_id,))
    user = cursor.fetchone()
    cursor.close()
    conn.close()
    
    return render_template("edit_user.html", user=user)


#This function fetches invoices based on user roles
@login_required
@app.route("/invoices", methods=["GET"])
def invoices():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Clients see only their own invoices
    if current_user.role == "Client":
        cursor.execute("SELECT * FROM Invoice WHERE UserID = %s", (current_user.id,))
    else:
        cursor.execute("SELECT * FROM Invoice")

    invoices = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("invoices.html", invoices=invoices)


#Add Invoice Creation
@login_required
@app.route("/add_invoice", methods=["GET", "POST"])
def add_invoice():
    if current_user.role not in ["Admin", "Accountant"]:
        flash("You don't have permission to add invoices.", "danger")
        return redirect(url_for("invoices"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        invoice_date = request.form["invoice_date"]
        due_date = request.form["due_date"]
        total_amount = request.form["total_amount"]
        status = "Unpaid"
        user_id = request.form["user_id"]
        account_id = request.form["account_id"]  # Ensure this is received

        # Insert the Invoice
        cursor.execute("""
            INSERT INTO Invoice (InvoiceDate, DueDate, TotalAmount, Status, UserID) 
            VALUES (%s, %s, %s, %s, %s)
        """, (invoice_date, due_date, total_amount, status, user_id))
        
        invoice_id = cursor.lastrowid  # Get the ID of the inserted invoice

        # Insert the Transaction (Revenue from the Invoice)
        cursor.execute("""
            INSERT INTO Transaction (TransactionType, TransactionCategory, InvoiceID, Description, Date, Amount, AccountID)
            VALUES ('Credit', 'Revenue', %s, 'Invoice #%s Issued', %s, %s, %s)
        """, (invoice_id, invoice_id, invoice_date, total_amount, account_id))

        conn.commit()
        cursor.close()
        conn.close()

        flash("Invoice added successfully!", "success")
        return redirect(url_for("invoices"))

    # Fetch accounts for selection
    cursor.execute("SELECT AccountID, AccountName FROM ChartOfAccounts")
    accounts = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("add_invoice.html", accounts=accounts)



#editing invoice
@login_required
@app.route("/edit_invoice/<int:invoice_id>", methods=["GET", "POST"])
def edit_invoice(invoice_id):
    if current_user.role not in ["Admin", "Accountant"]:
        flash("You don't have permission to edit invoices.", "danger")
        return redirect(url_for("invoices"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        invoice_date = request.form["invoice_date"]
        due_date = request.form["due_date"]
        total_amount = request.form["total_amount"]
        status = request.form["status"]

        cursor.execute("UPDATE Invoice SET InvoiceDate = %s, DueDate = %s, TotalAmount = %s, Status = %s WHERE InvoiceID = %s",
                       (invoice_date, due_date, total_amount, status, invoice_id))
        conn.commit()
        cursor.close()
        conn.close()

        flash("Invoice updated successfully!", "success")
        return redirect(url_for("invoices"))

    cursor.execute("SELECT * FROM Invoice WHERE InvoiceID = %s", (invoice_id,))
    invoice = cursor.fetchone()
    cursor.close()
    conn.close()

    return render_template("edit_invoice.html", invoice=invoice)


#delete invoice
@login_required
@app.route("/delete_invoice/<int:invoice_id>", methods=["POST"])
def delete_invoice(invoice_id):
    if current_user.role not in ["Admin", "Accountant"]:
        flash("You don't have permission to delete invoices.", "danger")
        return redirect(url_for("invoices"))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Invoice WHERE InvoiceID = %s", (invoice_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Invoice deleted successfully!", "success")
    return redirect(url_for("invoices"))

##link to payments
@login_required
@app.route("/payments", methods=["GET"])
def payments():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if current_user.role == "Client":
        cursor.execute("""
            SELECT p.*, i.InvoiceID FROM Payment p 
            JOIN Invoice i ON p.InvoiceID = i.InvoiceID 
            WHERE i.UserID = %s
        """, (current_user.id,))
    else:
        cursor.execute("SELECT * FROM Payment")

    payments = cursor.fetchall()
    cursor.close()
    conn.close()
    
    return render_template("payments.html", payments=payments)



#payment form
@login_required
@app.route("/add_payment", methods=["GET", "POST"])
def add_payment():
    if current_user.role not in ["Admin", "Accountant"]:
        flash("You don't have permission to add payments.", "danger")
        return redirect(url_for("payments"))

    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        payment_date = request.form["payment_date"]
        amount = float(request.form["amount"])
        method = request.form["payment_method"]
        invoice_id = request.form["invoice_id"]
        account_id = request.form["account_id"]  # Ensure this field is retrieved

        # Insert Payment Record
        cursor.execute("""
            INSERT INTO Payment (PaymentDate, Amount, PaymentMethod, InvoiceID) 
            VALUES (%s, %s, %s, %s)
        """, (payment_date, amount, method, invoice_id))

        payment_id = cursor.lastrowid  # Get the PaymentID

        # Insert Transaction (Debit - Money Received)
        # Insert Transaction (Debit - Money Received)
        cursor.execute("""
            INSERT INTO Transaction (TransactionType, TransactionCategory, PaymentID, InvoiceID, Description, Date, Amount, AccountID)
            VALUES ('Debit', 'Payment', %s, %s, %s, %s, %s, %s)
            """, (payment_id, invoice_id, f'Payment received for Invoice #{invoice_id}', payment_date, amount, account_id))


        # Calculate total payments for the invoice
        cursor.execute("SELECT SUM(Amount) as TotalPaid FROM Payment WHERE InvoiceID = %s", (invoice_id,))
        total_paid = cursor.fetchone()["TotalPaid"]

        # Get the Invoice Total Amount
        cursor.execute("SELECT TotalAmount FROM Invoice WHERE InvoiceID = %s", (invoice_id,))
        invoice_total = cursor.fetchone()["TotalAmount"]

        # Update Invoice Status based on payments
        if total_paid >= invoice_total:
            cursor.execute("UPDATE Invoice SET Status = 'Paid' WHERE InvoiceID = %s", (invoice_id,))
        else:
            cursor.execute("UPDATE Invoice SET Status = 'Partially Paid' WHERE InvoiceID = %s", (invoice_id,))

        conn.commit()
        cursor.close()
        conn.close()

        flash("Payment recorded. Invoice status updated.", "success")
        return redirect(url_for("payments"))

    # Fetch unpaid invoices and accounts for selection
    cursor.execute("SELECT InvoiceID FROM Invoice WHERE Status != 'Paid'")
    invoices = cursor.fetchall()
    cursor.execute("SELECT AccountID, AccountName FROM ChartOfAccounts")
    accounts = cursor.fetchall()
    cursor.close()
    conn.close()

    return render_template("add_payment.html", invoices=invoices, accounts=accounts)




# remove users
@login_required
@app.route("/delete_user/<int:user_id>", methods=["POST"])
def delete_user(user_id):
    if current_user.role != "Admin":
        flash("You don't have permission to delete users.", "danger")
        return redirect(url_for("dashboard"))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM User WHERE UserID = %s", (user_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("User deleted successfully!", "success")
    return redirect(url_for("list_users"))


# Logout Route
@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for("login"))

# Dashboard Route (Only logged-in users can access)
@app.route("/dashboard")
@login_required
def dashboard():
    return render_template("dashboard.html", name=current_user.name, role=current_user.role)

# Transactions Page
@login_required
@app.route("/transactions", methods=["GET", "POST"])
def transactions():
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    # Fetch accounts for filtering (only show accounts for the current user if Client)
    if current_user.role == "Client":
        cursor.execute("SELECT AccountID, AccountName FROM ChartOfAccounts WHERE UserID = %s", (current_user.id,))
    else:
        cursor.execute("SELECT AccountID, AccountName FROM ChartOfAccounts")
    
    accounts = cursor.fetchall()

    # Default query with joins to link invoices and payments
    query = """
        SELECT 
            t.TransactionID, t.Date, t.Amount, t.Description, t.TransactionType, 
            t.TransactionCategory, t.AccountID, i.InvoiceID, p.PaymentID
        FROM Transaction t
        LEFT JOIN Invoice i ON t.InvoiceID = i.InvoiceID
        LEFT JOIN Payment p ON t.PaymentID = p.PaymentID
        WHERE 1=1
    """
    params = []

    # Apply filters based on user input
    if request.method == "POST":
        start_date = request.form.get("start_date")
        end_date = request.form.get("end_date")
        amount = request.form.get("amount")
        transaction_type = request.form.get("transaction_type")
        account_id = request.form.get("account_id")

        if start_date:
            query += " AND t.Date >= %s"
            params.append(start_date)
        if end_date:
            query += " AND t.Date <= %s"
            params.append(end_date)
        if amount:
            query += " AND t.Amount = %s"
            params.append(amount)
        if transaction_type and transaction_type != "All":
            query += " AND t.TransactionType = %s"
            params.append(transaction_type)
        if account_id and account_id != "All":
            query += " AND t.AccountID = %s"
            params.append(account_id)

    query += " ORDER BY t.Date DESC"

    # Fetch filtered transactions
    cursor.execute(query, tuple(params))
    transactions = cursor.fetchall()
    
    cursor.close()
    conn.close()

    return render_template("transactions.html", transactions=transactions, accounts=accounts)


# Edit Transaction
@app.route("/edit_transaction/<int:transaction_id>", methods=["GET", "POST"])
@login_required
def edit_transaction(transaction_id):
    conn = get_db_connection()
    cursor = conn.cursor(dictionary=True)

    if request.method == "POST":
        if current_user.role not in ["Admin", "Accountant"]:
            flash("You don't have permission to edit transactions.", "danger")
            return redirect(url_for("transactions"))

        date = request.form["date"]
        amount = request.form["amount"]
        description = request.form["description"]
        transaction_type = request.form["transaction_type"]

        cursor.execute("UPDATE Transaction SET Date = %s, Amount = %s, Description = %s, TransactionType = %s WHERE TransactionID = %s", 
                       (date, amount, description, transaction_type, transaction_id))
        conn.commit()
        cursor.close()
        conn.close()
        flash("Transaction updated successfully!", "success")
        return redirect(url_for("transactions"))

    cursor.execute("SELECT * FROM Transaction WHERE TransactionID = %s", (transaction_id,))
    transaction = cursor.fetchone()
    cursor.close()
    conn.close()
    return render_template("edit_transaction.html", transaction=transaction)

# Delete Transaction
@app.route("/delete_transaction/<int:transaction_id>", methods=["POST"])
@login_required
def delete_transaction(transaction_id):
    if current_user.role not in ["Admin", "Accountant"]:
        flash("You don't have permission to delete transactions.", "danger")
        return redirect(url_for("transactions"))

    conn = get_db_connection()
    cursor = conn.cursor()
    cursor.execute("DELETE FROM Transaction WHERE TransactionID = %s", (transaction_id,))
    conn.commit()
    cursor.close()
    conn.close()

    flash("Transaction deleted successfully!", "success")
    return redirect(url_for("transactions"))

if __name__ == "__main__":
    app.run(debug=True)
