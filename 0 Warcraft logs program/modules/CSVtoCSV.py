import csv

def load_csv(file_path, output_path):
    '''
    Load a CSV file, filter for specific event types, and save to a new CSV.

    Approach:
    - The script reads a combat log CSV line by line.
    - It categorizes events based on their type and extracts relevant data.
    - Different event types have different structures, so specific indices are used to pull needed values.
    - The filtered data is written to a new CSV file with a consistent format for ease of analysis.

    Event Categories:
    - SPELL_AURA (buffs/debuffs) → Extracts spell destination, ID, name, and aura type.
    - ENCOUNTER (start/end) → Extracts map ID and encounter name.
    - DAMAGE/HEAL events (spells and ranged attacks) → Extracts damage source, destination, spell details, and position data.
    - SWING_DAMAGE (melee attacks) → Extracts similar details but with different positional indices.
    - UNIT_DIED (death events) → Extracts the entity that died.

     Header Structure:
    The header structure was chosen to maintain consistency across different event types while ensuring that all relevant data points are captured 
    for analysis. Some events have different available fields (e.g., SWING vs. SPELL_AURA), 
    so missing values are left as empty strings to maintain a uniform format. This approach allows for easier post-processing and ensures all event
    types fit within a standardized dataset.

     CSV Structure:
    The input CSV follows a structured event logging format where:
    - The **first column (Index 0)** always represents the `timestamp` of the event.
    - The **second column (Index 1)** is the `event type`, which determines how the row is processed.
    - Based on `event type`, specific indices are accessed to extract relevant fields.
    - Position-related data (X, Y coordinates) vary depending on the event type, requiring conditional handling.
    
    '''    
    try:
        with open(file_path, mode='r', encoding='utf-8') as file, \
             open(output_path, mode='w', encoding='utf-8', newline='') as outfile:
            
            reader = csv.reader(file)
            writer = csv.writer(outfile)
            
            # Write header for new CSV
            writer.writerow(["timestamp", "event type", "Damage source", "Spell destination", "spell id", "spell name", "X coord", "Y coord", "Facing direction", "Aura type", "map id", "encounter name"])
            
            for row in reader:
                if not row:
                    continue  # Skip empty rows
                
                timestamp, event_type = row[:2]  # Always index 0 and 1
                
                if event_type in ["SPELL_AURA_REMOVED", "SPELL_AURA_REFRESH", "SPELL_AURA_APPLIED"]:
                    spell_dest = row[2]
                    spell_id = row[3]
                    spell_name = row[4]
                    aura_type = row[5]
                    writer.writerow([timestamp, event_type, "", spell_dest, spell_id, spell_name, "", "", "", aura_type, "", ""])
                
                elif event_type in ["ENCOUNTER_START", "ENCOUNTER_END"]:
                    map_id = row[2]
                    encounter_name = row[4]
                    writer.writerow([timestamp, event_type, "", "", "", "", "", "", "", "", map_id, encounter_name])
                
                elif event_type in ["RANGE_DAMAGE", "SPELL_CAST_SUCCESS", "SPELL_HEAL", "SPELL_DAMAGE", "SPELL_PERIODIC_DAMAGE", "SPELL_PERIODIC_HEAL"]:
                    damage_source = row[3]
                    spell_dest = row[7]
                    spell_id = row[10]
                    spell_name = row[11]
                    x_coord = row[27]
                    y_coord = row[28]
                    facing_direction = row[30]
                    writer.writerow([timestamp, event_type, damage_source, spell_dest, spell_id, spell_name, x_coord, y_coord, facing_direction, "", "", ""])
                
                elif event_type in ["SWING_DAMAGE", "SWING_DAMAGE_LANDED"]:
                    damage_source = row[3]
                    spell_dest = row[7]
                    spell_id = row[10]
                    x_coord = row[24]  # Different indices for position data
                    y_coord = row[25]
                    facing_direction = row[27]
                    writer.writerow([timestamp, event_type, damage_source, spell_dest, spell_id, "", x_coord, y_coord, facing_direction, "", "", ""])
                
                elif event_type == "UNIT_DIED":
                    spell_dest = row[7]  # The player/NPC that died
                    writer.writerow([timestamp, event_type, "", spell_dest, "", "", "", "", "", "", "", ""])
            
        print(f"Filtered CSV successfully created: {output_path}")
    except Exception as e:
        print(f"Error processing CSV: {e}")

# Example usage
file_path = r"C:\Users\alanw\Documents\GitHub\Class\0 Warcraft logs program\modules\combat_log_with_floats.csv"
output_path = r"C:\Users\alanw\Documents\GitHub\Class\0 Warcraft logs program\modules\filtered_combat_log.csv"
load_csv(file_path, output_path)
