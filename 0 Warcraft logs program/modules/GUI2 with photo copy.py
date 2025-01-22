import tkinter as tk
from tkinter import ttk
import pandas as pd
import os
import matplotlib.pyplot as plt
import seaborn as sns

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the parsed CSV file path
parsed_csv_path = os.path.join(script_dir, "filtered_combat_log.csv")

# Define the background image path
background_image_path = os.path.join(script_dir, "plan.png")

# Load the parsed CSV file
df = pd.read_csv(parsed_csv_path, dtype=str)

# Ensure required columns exist
required_columns = ["event type", "spell name", "X coord", "Y coord"]
if not all(col in df.columns for col in required_columns):
    raise ValueError("One or more required columns are missing from the parsed CSV file.")

# Convert Position X and Y to numeric values
df["X coord"] = pd.to_numeric(df["X coord"], errors='coerce')
df["Y coord"] = pd.to_numeric(df["Y coord"], errors='coerce')

# Drop rows with missing coordinates
df = df.dropna(subset=["X coord", "Y coord"])

# Create a list of unique event types and spell names for filtering
unique_events = sorted(df["event type"].dropna().unique().tolist())
unique_spells = sorted(df["spell name"].dropna().unique().tolist())

# Function to plot location data with background image
def plot_scatter():
    event_type = event_type_combo.get().strip()
    spell_name = spell_entry.get().strip()
    
    query = (df["event type"] == event_type)
    if spell_name:
        query &= df["spell name"].str.contains(spell_name, case=False, na=False)
    
    filtered_df = df[query]
    
    if filtered_df.empty:
        result_label.config(text="No matching data found.")
    else:
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Load and display background image using figimage()
        img = plt.imread(background_image_path)
        fig.figimage(img, xo=0, yo=0, alpha=0.6, zorder=0)
        
        ax.scatter(filtered_df["X coord"], filtered_df["Y coord"], alpha=0.6, color='blue', zorder=1)
        ax.set_title(f"Scatter Plot - {event_type} ({spell_name if spell_name else 'All Spells'})")
        ax.set_xlabel("X coord")
        ax.set_ylabel("Y coord")
        ax.grid()
        plt.show()

# Function to generate a heatmap with background image
def plot_heatmap():
    event_type = event_type_combo.get().strip()
    spell_name = spell_entry.get().strip()
    
    query = (df["event type"] == event_type)
    if spell_name:
        query &= df["spell name"].str.contains(spell_name, case=False, na=False)
    
    filtered_df = df[query]
    
    if filtered_df.empty:
        result_label.config(text="No matching data found.")
    else:
        fig, ax = plt.subplots(figsize=(8, 6))
        
        # Load and display background image using figimage()
        img = plt.imread(background_image_path)
        fig.figimage(img, xo=0, yo=0, alpha=0.6, zorder=0)
        
        sns.kdeplot(x=filtered_df["X coord"], y=filtered_df["Y coord"], cmap="Reds", fill=True, alpha=0.6, ax=ax, zorder=1)
        ax.set_title(f"Heatmap - {event_type} ({spell_name if spell_name else 'All Spells'})")
        ax.set_xlabel("X coord")
        ax.set_ylabel("Y coord")
        ax.grid()
        plt.show()

# Create Tkinter window
root = tk.Tk()
root.title("WoW Combat Log Location Visualizer")

# UI Components
tk.Label(root, text="Select Event Type:").pack(pady=5)
event_type_combo = ttk.Combobox(root, values=unique_events, state="readonly")
event_type_combo.pack(pady=5)
event_type_combo.set(unique_events[0])

tk.Label(root, text="Enter Spell Name (optional):").pack(pady=5)
spell_entry = tk.Entry(root, width=30)
spell_entry.pack(pady=5)

plot_scatter_button = tk.Button(root, text="Plot Scatter", command=plot_scatter)
plot_scatter_button.pack(pady=5)

plot_heatmap_button = tk.Button(root, text="Plot Heatmap", command=plot_heatmap)
plot_heatmap_button.pack(pady=5)

result_label = tk.Label(root, text="")
result_label.pack(pady=5)

# Run the Tkinter event loop
root.mainloop()
