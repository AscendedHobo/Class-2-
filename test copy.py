import pandas as pd

# File path
file_path = r"C:\Users\alanw\Documents\GitHub\Class\0 Warcraft logs program\modules\filtered_combat_log.csv"

# Load the CSV file
df = pd.read_csv(file_path)

# Display the description
print(df.describe(include='all'))
