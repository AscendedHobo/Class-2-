import os
import csv
import re

# Define the input log file path
log_file_path = r"C:\Users\alanw\Desktop\Split-2025-01-19T190125.449Z-QueenAnsurek Mythic.txt"

# Get the directory where the script is located
script_dir = os.path.dirname(os.path.abspath(__file__))

# Define the output filtered log CSV file path
floats_csv_path = os.path.join(script_dir, "combat_log_with_floats.csv")

# List of metadata event types to exclude
excluded_events = {"COMBAT_LOG_VERSION", "MAP_CHANGE", "COMBATANT_INFO"}

# List of encounter tracking, death, and spell aura events to keep
included_events = {"ENCOUNTER_START", "ENCOUNTER_END", "UNIT_DIED", "SPELL_AURA_APPLIED", 
                  "SPELL_AURA_REMOVED", "SPELL_AURA_REFRESH"}

# Function to process aura events into structured format
def process_aura_event(timestamp, event_fields):
    try:
        # Extract relevant fields from the aura event
        event_type = event_fields[0]
        source_guid = event_fields[1]
        source_name = event_fields[2].strip('"')  # Remove quotes
        dest_guid = event_fields[5]
        dest_name = event_fields[6].strip('"')    # Remove quotes
        spell_id = event_fields[9]
        spell_name = event_fields[10].strip('"')  # Remove quotes
        aura_type = event_fields[-1]              # BUFF or DEBUFF
        
        # Return structured format
        return [
            timestamp,
            event_type,
            dest_name,      # Destination player name
            spell_id,
            spell_name,
            aura_type
        ]
    except (IndexError, Exception) as e:
        print(f"Error processing aura event: {e}")
        print(f"Event fields: {event_fields}")
        return None

# Read the combat log and filter lines
filtered_data = []

# Regex pattern to match only floating-point numbers (must have a decimal)
float_pattern = re.compile(r"[-+]?[0-9]*\.[0-9]+")

with open(log_file_path, "r", encoding="utf-8") as infile:
    for line in infile:
        # Ensure the line has at least two parts (timestamp + event)
        if len(line.strip()) < 25:
            continue  # Skip malformed lines
        
        timestamp_part = line[:24]  # Extract fixed-length timestamp
        event_part = line[25:].strip()  # Extract the rest of the event line
        
        # Extract event type (first value after timestamp)
        event_type = event_part.split(",", 1)[0]
        
        # Skip explicitly excluded events
        if event_type in excluded_events:
            continue
        
        # Handle aura events specially
        if event_type in {"SPELL_AURA_APPLIED", "SPELL_AURA_REMOVED", "SPELL_AURA_REFRESH"}:
            # Parse the event line properly handling quoted fields
            event_fields = next(csv.reader([event_part], delimiter=','))
            processed_event = process_aura_event(timestamp_part, event_fields)
            if processed_event:
                filtered_data.append(processed_event)
            continue
            
        # Handle other included events
        if event_type in included_events:
            event_fields = next(csv.reader([event_part], delimiter=','))
            filtered_data.append([timestamp_part] + event_fields)
            continue
            
        # Use regex to check if the event part contains floating-point numbers
        if float_pattern.search(event_part):
            event_fields = next(csv.reader([event_part], delimiter=','))
            filtered_data.append([timestamp_part] + event_fields)

# Define headers for the CSV file
headers = ["Timestamp", "Event Type", "Destination Player", "Spell ID", "Spell Name", "Aura Type"]

# Save filtered lines to a CSV file
with open(floats_csv_path, "w", encoding="utf-8", newline='') as outfile:
    writer = csv.writer(outfile, quoting=csv.QUOTE_MINIMAL)
    writer.writerow(headers)  # Write headers
    writer.writerows(filtered_data)

print(f"Combat log lines containing floats, death events, and spell auras saved to: {floats_csv_path}")