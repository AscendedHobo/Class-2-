import re
import os
import csv

def track_event_variations(log_file):
    tracked_events = {
        "SPELL_AURA_APPLIED", "SPELL_AURA_REMOVED", "SPELL_AURA_APPLIED_DOSE", 
        "SPELL_AURA_REMOVED_DOSE", "SPELL_AURA_REFRESH", "SPELL_DAMAGE", 
        "SPELL_PERIODIC_DAMAGE", "SWING_DAMAGE", "UNIT_DIED", "SPELL_CAST_SUCCESS"
    }
    
    event_seen = {}
    base_dir = os.path.dirname(log_file)
    txt_output_file = os.path.join(base_dir, "event_variations.txt")
    csv_output_file = os.path.join(base_dir, "event_variations.csv")
    
    with open(log_file, 'r', encoding='utf-8') as file:
        log_lines = file.readlines()
    
    with open(txt_output_file, 'w', encoding='utf-8') as txt_out, open(csv_output_file, 'w', encoding='utf-8', newline='') as csv_out:
        csv_writer = csv.writer(csv_out)
        csv_writer.writerow(["Event Type", "Item Count", "Timestamp", "Details"])
        
        for line in log_lines:
            parts = line.strip().split(',')  # Split line by commas
            match = re.match(r'(\d+/\d+/\d+ \d+:\d+:\d+\.\d+)\s+([A-Z_]+)', parts[0])
            if match:
                timestamp = match.group(1)
                event_type = match.group(2)
                if event_type in tracked_events:
                    length = len(parts)
                    
                    if event_type not in event_seen:
                        event_seen[event_type] = {}
                    
                    if length not in event_seen[event_type]:
                        event_seen[event_type][length] = parts
        
        for event_type, length_dict in event_seen.items():
            txt_out.write(f"{event_type}\n")
            txt_out.write("=" * len(event_type) + "\n")
            for length, log_parts in length_dict.items():
                txt_out.write(f"Found with {length} items:\n")
                txt_out.write("-" * 20 + "\n")
                txt_out.write(", ".join(log_parts) + "\n\n")
                csv_writer.writerow([event_type, length, log_parts[0], *log_parts[1:]])
    
    print("Tracking complete. Data saved to", txt_output_file, "and", csv_output_file)

# Example usage
log_file_path = r"C:\\Program Files (x86)\\World of Warcraft\\_retail_\\Logs\\warcraftlogsarchive\\Archive-WoWCombatLog-011825_145146.txt"  # Replace with actual file path
track_event_variations(log_file_path)
