import pandas as pd
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the input filtered CSV file path
filtered_csv_path = os.path.join(script_dir, "filtered_combat_log.csv")

# Define the output parsed CSV file path
parsed_csv_path = os.path.join(script_dir, "parsed_combat_log.csv")

# List of essential columns to keep per event type
core_columns = ["Timestamp", "Event Type", "Source GUID", "Source Name", "Dest GUID", "Dest Name", "Position X", "Position Y"]

event_specific_columns = {
    "SPELL_DAMAGE": ["Spell ID", "Spell Name", "Amount", "Damage Type"],
    "SPELL_PERIODIC_DAMAGE": ["Spell ID", "Spell Name", "Amount", "Damage Type"],
    "SWING_DAMAGE": ["Amount"],
    "SPELL_AURA_APPLIED": ["Spell ID", "Spell Name", "Amount"],
    "SPELL_AURA_REMOVED": ["Spell ID", "Spell Name", "Amount"],
    "SPELL_AURA_APPLIED_DOSE": ["Spell ID", "Spell Name", "Amount"],
    "SPELL_AURA_REMOVED_DOSE": ["Spell ID", "Spell Name", "Amount"],
    "SPELL_PERIODIC_HEAL": ["Spell ID", "Spell Name", "Amount"],
    "SPELL_CAST_SUCCESS": ["Spell ID", "Spell Name"],
    "UNIT_DIED": []  # Only core columns are needed
}

# Read the filtered CSV file into a Pandas DataFrame
df = pd.read_csv(filtered_csv_path, dtype=str)

# Dynamically filter columns per event type
filtered_rows = []
for _, row in df.iterrows():
    event_type = row["Event Type"]
    
    if event_type in event_specific_columns:
        selected_columns = core_columns + event_specific_columns[event_type]
        filtered_rows.append(row[selected_columns].to_dict())

# Convert the filtered data back into a DataFrame
parsed_df = pd.DataFrame(filtered_rows)

# Ensure numerical columns are correctly formatted
numeric_columns = ["Amount", "Position X", "Position Y"]
for col in numeric_columns:
    if col in parsed_df.columns:
        parsed_df[col] = pd.to_numeric(parsed_df[col], errors='coerce')

# Save the parsed CSV file
parsed_df.to_csv(parsed_csv_path, index=False)

print(f"Parsed combat log saved to: {parsed_csv_path}")
