import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the parsed CSV file path
parsed_csv_path = os.path.join(script_dir, "parsed_combat_log.csv")

# Load the parsed CSV file
df = pd.read_csv(parsed_csv_path, dtype=str)

# Ensure required columns exist
required_columns = ["Dest Name", "Spell ID", "Spell Name", "Event Type", "Position X", "Position Y", "Timestamp"]
if not all(col in df.columns for col in required_columns):
    raise ValueError("One or more required columns are missing from the parsed CSV file.")

# Create a list of unique player names for autocomplete
unique_players = sorted(df["Dest Name"].dropna().unique().tolist())

# Function to search for spell occurrences and return positional data
def search_spells():
    player_name = player_entry.get().strip()
    spell_id = spell_entry.get().strip()
    spell_name = spell_name_entry.get().strip()
    
    if not player_name and not spell_id and not spell_name:
        result_label.config(text="Enter a player name, spell ID, or spell name to search.")
        return

    # Filter DataFrame based on input
    query = (df["Dest Name"].str.contains(player_name, case=False, na=False) if player_name else True) & \
            (df["Spell ID"] == spell_id if spell_id else True) & \
            (df["Spell Name"].str.contains(spell_name, case=False, na=False) if spell_name else True)
    result_df = df[query]
    
    if result_df.empty:
        result_label.config(text="No occurrences found.")
    else:
        results = []
        for _, row in result_df.iterrows():
            # Find the closest SPELL_CAST_SUCCESS event BEFORE the aura application
            cast_query = (df["Spell ID"] == row["Spell ID"]) & (df["Event Type"] == "SPELL_CAST_SUCCESS")
            cast_df = df[cast_query].sort_values(by="Timestamp", ascending=True)
            cast_df = cast_df[cast_df["Timestamp"] <= row["Timestamp"]]  # Only consider casts before the application
            
            if not cast_df.empty:
                cast_event = cast_df.iloc[-1]  # Get the most recent matching cast event before application
                results.append(f"Buff/Debuff Applied: {row['Timestamp']} | X: {cast_event['Position X']} | Y: {cast_event['Position Y']}")
            
            # Find last periodic tick to estimate removal location
            tick_query = (df["Spell ID"] == row["Spell ID"]) & (df["Event Type"] == "SPELL_PERIODIC_DAMAGE")
            tick_df = df[tick_query].sort_values(by="Timestamp", ascending=True)
            tick_df = tick_df[tick_df["Timestamp"] >= row["Timestamp"]]  # Only consider ticks after application
            
            if not tick_df.empty:
                last_tick = tick_df.iloc[-1]
                results.append(f"Buff/Debuff Removed (Estimated): {last_tick['Timestamp']} | X: {last_tick['Position X']} | Y: {last_tick['Position Y']}")

        # Display results
        result_text.delete("1.0", tk.END)  # Clear previous results
        result_text.insert(tk.END, "\n".join(results))

# Function to update autocomplete suggestions
def update_suggestions(event):
    input_text = player_entry.get().strip().lower()
    matches = [name for name in unique_players if input_text in name.lower()]
    name_listbox.delete(0, tk.END)
    for match in matches:
        name_listbox.insert(tk.END, match)

# Function to fill player entry with selected name
def fill_player_entry(event):
    selected = name_listbox.get(name_listbox.curselection())
    player_entry.delete(0, tk.END)
    player_entry.insert(0, selected)
    name_listbox.delete(0, tk.END)

# Create Tkinter window
root = tk.Tk()
root.title("WoW Combat Log Search - Buff/Debuff Locations")

# UI Components
tk.Label(root, text="Enter Player Name:").pack(pady=5)
player_entry = tk.Entry(root, width=30)
player_entry.pack(pady=5)

# Autocomplete Listbox
name_listbox = tk.Listbox(root, height=5)
name_listbox.pack(pady=5)
player_entry.bind("<KeyRelease>", update_suggestions)
name_listbox.bind("<<ListboxSelect>>", fill_player_entry)

tk.Label(root, text="Enter Spell ID:").pack(pady=5)
spell_entry = tk.Entry(root, width=30)
spell_entry.pack(pady=5)

tk.Label(root, text="Enter Spell Name:").pack(pady=5)
spell_name_entry = tk.Entry(root, width=30)
spell_name_entry.pack(pady=5)

search_button = tk.Button(root, text="Search", command=search_spells)
search_button.pack(pady=5)

result_text = tk.Text(root, height=15, width=70)
result_text.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
