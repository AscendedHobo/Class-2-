import pandas as pd
import os

# Define file paths
input_csv_path = r"C:\Users\alanw\Documents\GitHub\Class\0 Warcraft logs program\modules\combat_log_with_floats.csv"
output_csv_path = os.path.join(os.path.dirname(input_csv_path), "combat_log_updated_swing_positions.csv")

# Load the filtered CSV into a DataFrame
df = pd.read_csv(input_csv_path, dtype=str)

# Ensure required columns exist
if len(df.columns) < 30:
    raise ValueError("Unexpected column count. Ensure the input CSV has at least 30 columns.")

# Identify swing damage events and move X, Y position data from columns 25, 26 to 28, 29
df.loc[df["Field_0"].isin(["SWING_DAMAGE", "SWING_DAMAGE_LANDED"]), "Field_28"] = df.loc[df["Field_0"].isin(["SWING_DAMAGE", "SWING_DAMAGE_LANDED"]), "Field_25"]
df.loc[df["Field_0"].isin(["SWING_DAMAGE", "SWING_DAMAGE_LANDED"]), "Field_29"] = df.loc[df["Field_0"].isin(["SWING_DAMAGE", "SWING_DAMAGE_LANDED"]), "Field_26"]

# Save the updated DataFrame to a new CSV file
df.to_csv(output_csv_path, index=False)

print(f"Swing damage positions updated and saved to: {output_csv_path}")
