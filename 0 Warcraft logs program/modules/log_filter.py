import os
import csv
import re

# Define the input log file path
log_file_path = r"C:\Program Files (x86)\World of Warcraft\_retail_\Logs\warcraftlogsarchive\Archive-WoWCombatLog-011825_145146.txt"

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the output filtered log CSV file path
floats_csv_path = os.path.join(script_dir, "combat_log_with_floats.csv")

# Read the combat log and filter lines containing floats
filtered_data = []

# Regex pattern to match only floating-point numbers (must have a decimal)
float_pattern = re.compile(r"[-+]?[0-9]*\.[0-9]+")

# List of metadata events to exclude
exclude_events = {"COMBAT_LOG_VERSION", "MAP_CHANGE"}

with open(log_file_path, "r", encoding="utf-8") as infile:
    for line in infile:
        # Ensure the line has at least two parts (timestamp + event)
        if len(line.strip()) < 25:
            continue  # Skip malformed lines
        
        timestamp_part = line[:24]  # Extract fixed-length timestamp
        event_part = line[25:].strip()  # Extract the rest of the event line
        
        # Extract event type
        event_type = event_part.split(",")[0]
        
        # Skip metadata events
        if event_type in exclude_events:
            continue
        
        # Use regex to check if the event part (excluding timestamp) contains floating-point numbers
        if float_pattern.search(event_part):
            # Properly split event data while keeping quoted text together
            event_fields = next(csv.reader([event_part], delimiter=','))
            filtered_data.append([timestamp_part] + event_fields)

# Save filtered lines to a CSV file
with open(floats_csv_path, "w", encoding="utf-8", newline='') as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(["Timestamp"] + [f"Field_{i}" for i in range(len(filtered_data[0]) - 1)])  # Headers
    writer.writerows(filtered_data)  # Write filtered log lines

print(f"Combat log lines containing floats saved to: {floats_csv_path}")