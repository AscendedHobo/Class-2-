import pandas as pd
import os

# Define the input filtered CSV file path
csv_file_path = r"C:\Users\alanw\Documents\GitHub\Class\0 Warcraft logs program\modules\combat_log_with_floats.csv"

# Load the CSV into a Pandas DataFrame, skipping malformed rows
df = pd.read_csv(csv_file_path, dtype=str, on_bad_lines="skip")

# Define event types to sample from
event_types = [
    "DAMAGE_SPLIT", "SPELL_CAST_SUCCESS", "SPELL_DAMAGE", "SPELL_DAMAGE_SUPPORT",
    "SPELL_ENERGIZE", "SPELL_HEAL", "SPELL_PERIODIC_DAMAGE", "SPELL_PERIODIC_ENERGIZE",
    "SPELL_PERIODIC_HEAL", "SWING_DAMAGE", "SWING_DAMAGE_LANDED"
]

# Sample first 5 occurrences of each event type
sampled_data = []
for event in event_types:
    event_subset = df[df["Field_0"] == event].head(5)
    sampled_data.append(event_subset)

# Concatenate sampled data into a single DataFrame
sampled_df = pd.concat(sampled_data)

# Save to a CSV file for easy review
output_file_path = os.path.join(os.path.dirname(csv_file_path), "sampled_combat_log.csv")
sampled_df.to_csv(output_file_path, index=False)

print(f"Sampled event lines saved to: {output_file_path}")
