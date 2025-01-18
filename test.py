import os

base_path = r"C:\Users\alanw\Documents\GitHub\Class\account pro 2"

folders = [
    os.path.join(base_path, "templates", "users"),
    os.path.join(base_path, "static", "css"),
    os.path.join(base_path, "static", "js"),
]

for folder in folders:
    os.makedirs(folder, exist_ok=True)

print("Folders created successfully.")
