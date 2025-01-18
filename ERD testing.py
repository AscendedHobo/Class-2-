from graphviz import Digraph

# Create a new ERD diagram
erd = Digraph('ERD', filename=r'C:\Users\alanw\Desktop\bookkeeping_erd', format='png')

# Define entities
entities = {
    "Clients": ["client_id (PK)", "name", "contact_info"],
    "Invoices": ["invoice_id (PK)", "client_id (FK)", "date", "total_amount", "status"],
    "Payments": ["payment_id (PK)", "invoice_id (FK)", "date", "amount"],
    "Expenses": ["expense_id (PK)", "category_id (FK)", "supplier_id (FK)", "employee_id (FK)", "date", "amount", "description"],
    "Expense Categories": ["category_id (PK)", "name"],
    "Suppliers": ["supplier_id (PK)", "name", "contact_info"],
    "Projects": ["project_id (PK)", "client_id (FK)", "name", "start_date", "end_date"],
    "Employees": ["employee_id (PK)", "name", "role", "pay_rate"],
    "Payroll": ["payroll_id (PK)", "employee_id (FK)", "date", "hours_worked", "amount_paid"],
    "Bank Accounts": ["account_id (PK)", "name", "balance"],
    "Transactions": ["transaction_id (PK)", "account_id (FK)", "date", "type (income/expense)", "amount", "description"]
}

# Add entities to the diagram
for entity, attributes in entities.items():
    label = f"{entity}|" + r"\l".join(attributes) + r"\l"
    erd.node(entity, label=label, shape="record")

# Define relationships
relationships = [
    ("Clients", "Invoices", "1:N"),
    ("Invoices", "Payments", "1:N"),
    ("Expense Categories", "Expenses", "1:N"),
    ("Suppliers", "Expenses", "1:N"),
    ("Clients", "Projects", "1:N"),
    ("Projects", "Invoices", "1:N"),
    ("Projects", "Expenses", "1:N"),
    ("Employees", "Payroll", "1:N"),
    ("Employees", "Expenses", "1:N"),  # Employees linked to expenses if needed
    ("Bank Accounts", "Transactions", "1:N"),  # Track all bank-related transactions
    ("Payroll", "Transactions", "1:N"),  # Payroll payments recorded as transactions
    ("Payments", "Transactions", "1:N")  # Client payments recorded as transactions
]

# Add relationships to the diagram
for entity1, entity2, cardinality in relationships:
    erd.edge(entity1, entity2, label=cardinality)

# Render and save ERD
erd.render(format="png", cleanup=True)
