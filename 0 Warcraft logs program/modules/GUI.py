import tkinter as tk
from tkinter import ttk
import pandas as pd
import os

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the parsed CSV file path
parsed_csv_path = os.path.join(script_dir, "filtered_combat_log_final.csv")

# Load the parsed CSV file
df = pd.read_csv(parsed_csv_path, dtype=str)

# Ensure required columns exist
required_columns = ["Dest Name", "Spell ID", "Spell Name", "Event Type", "Timestamp", "Position X", "Position Y"]
if not all(col in df.columns for col in required_columns):
    raise ValueError("One or more required columns are missing from the parsed CSV file.")

# Create a list of unique player names, spell names, and event types for autocomplete
unique_players = sorted(df["Dest Name"].dropna().unique().tolist())
unique_spells = sorted(df["Spell Name"].dropna().unique().tolist())
unique_events = sorted(df["Event Type"].dropna().unique().tolist())

# Function to search for spell occurrences
def search_spells():
    player_name = player_entry.get().strip()
    spell_input = spell_entry.get().strip()
    event_type_filter = event_type_combo.get().strip()
    
    if not spell_input:
        result_label.config(text="Enter a spell ID or name to search.")
        return

    # Determine if spell input is an ID (integer) or name (string)
    if spell_input.isdigit():
        query = df["Spell ID"] == spell_input
    else:
        query = df["Spell Name"].str.contains(spell_input, case=False, na=False)
    
    if player_name:
        query &= df["Dest Name"].str.contains(player_name, case=False, na=False)
    
    if event_type_filter and event_type_filter != "All Events":
        query &= df["Event Type"] == event_type_filter
    
    result_df = df[query]
    
    if result_df.empty:
        result_label.config(text="No occurrences found.")
    else:
        results = result_df[["Timestamp", "Dest Name", "Event Type", "Position X", "Position Y"]].dropna().values.tolist()
        result_text.delete("1.0", tk.END)  # Clear previous results
        result_text.insert(tk.END, "Spell Events Found:\n")
        for entry in results:
            result_text.insert(tk.END, f"Timestamp: {entry[0]}, {entry[1]} took {entry[2]} at location X: {entry[3]}, Y: {entry[4]}\n")

# Function to update autocomplete suggestions
def update_suggestions(event, entry_box, suggestion_listbox, unique_values):
    input_text = entry_box.get().strip().lower()
    matches = [name for name in unique_values if input_text in name.lower()]
    suggestion_listbox.delete(0, tk.END)
    for match in matches:
        suggestion_listbox.insert(tk.END, match)

# Function to fill entry with selected name
def fill_entry(event, entry_box, suggestion_listbox):
    selected = suggestion_listbox.get(suggestion_listbox.curselection())
    entry_box.delete(0, tk.END)
    entry_box.insert(0, selected)
    suggestion_listbox.delete(0, tk.END)

# Create Tkinter window
root = tk.Tk()
root.title("WoW Combat Log Search - Player & Spell Query")

# UI Components
tk.Label(root, text="Enter Player Name (optional):").pack(pady=5)
player_entry = tk.Entry(root, width=30)
player_entry.pack(pady=5)

# Autocomplete Listbox for Player Names
player_listbox = tk.Listbox(root, height=5)
player_listbox.pack(pady=5)
player_entry.bind("<KeyRelease>", lambda event: update_suggestions(event, player_entry, player_listbox, unique_players))
player_listbox.bind("<<ListboxSelect>>", lambda event: fill_entry(event, player_entry, player_listbox))

tk.Label(root, text="Enter Spell ID or Name:").pack(pady=5)
spell_entry = tk.Entry(root, width=30)
spell_entry.pack(pady=5)

# Autocomplete Listbox for Spells
spell_listbox = tk.Listbox(root, height=5)
spell_listbox.pack(pady=5)
spell_entry.bind("<KeyRelease>", lambda event: update_suggestions(event, spell_entry, spell_listbox, unique_spells))
spell_listbox.bind("<<ListboxSelect>>", lambda event: fill_entry(event, spell_entry, spell_listbox))

# Event Type Dropdown
tk.Label(root, text="Select Event Type:").pack(pady=5)
event_type_combo = ttk.Combobox(root, values=["All Events"] + unique_events, state="readonly")
event_type_combo.pack(pady=5)
event_type_combo.set("All Events")

search_button = tk.Button(root, text="Search", command=search_spells)
search_button.pack(pady=5)

result_text = tk.Text(root, height=15, width=150)
result_text.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
