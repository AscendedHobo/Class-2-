import pyautogui
import time
import random
import tkinter as tk
from threading import Thread

# Gold tracking code
gold_refs = [
    (209, 186, 55), (208, 188, 65), (209, 190, 66), (239, 226, 84),
    (251, 224, 82), (255, 232, 82), (254, 222, 75), (255, 233, 79),
    (250, 225, 80), (255, 230, 74)
]
no_gold_ref = (27, 27, 27)
gold_positions = [
    (1129, 1402), (1188, 1396), (1253, 1395), (1301, 1400),
    (1350, 1399), (1404, 1399), (1469, 1398), (1519, 1395),
    (1577, 1395), (1630, 1401)
]

def get_rgb_at_position(x, y): 
    return pyautogui.screenshot(region=(x, y, 1, 1)).getpixel((0, 0))

def is_gold_color(rgb, tolerance=30):
    for ref in gold_refs:
        if all(abs(rgb[i] - ref[i]) <= tolerance for i in range(3)):
            return True
    return False

def count_gold():
    gold_count = 0
    for x, y in gold_positions:
        rgb = get_rgb_at_position(x, y)
        if rgb != no_gold_ref and is_gold_color(rgb):
            gold_count += 1
    return gold_count

# Minion checking code
regions = [
    (1049, 1197, 151, 120),  # Slot 1
    (1205, 1197, 127, 114),  # Slot 2
    (1356, 1201, 148, 106),  # Slot 3
    (1511, 1201, 134, 111)   # Slot 4
]

image_paths = [
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Bandit 1.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\DI miner 2.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Emp 4.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Gryf 2.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Pyro 3.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Ranger 5.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Rat miner 1.png",
    r"C:\Users\alanw\Desktop\Rumble botting\Unit icons\Troll 3.png"
]

def check_images_in_regions(image_paths, regions):
    minis_in_hand = []  # Initialize the list to store the minions found in regions
    
    for i, region in enumerate(regions, 1):
        for image_path in image_paths:
            try:
                result = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                if result:
                    minion_name = image_path.split("\\")[-1].replace(".png", "")  # Extract the minion name
                    minis_in_hand.append(minion_name)  # Add the minion name to the list
                    break  # Exit after first image is found in this region
            except Exception:
                # Suppress error messages for image checking
                pass

    return minis_in_hand  # Return the list of found minions

# Play selection logic
def select_best_play(minis_in_hand, gold_count):
    # If gold is 5 or more, play Troll or Ranger if available

    if gold_count >= 4:
        if "Emp 4" in minis_in_hand:
            return "Emp 4"

    if gold_count >= 5:
        if "Ranger 5" in minis_in_hand:
            return "Ranger 5"
        elif "Troll 3" in minis_in_hand:
            return "Troll 3"
    
    # If gold is less than 5 and we don't have enough to play Troll or Ranger, don't play anything
    elif gold_count < 5:
        if "Ranger 5 " in minis_in_hand or "Troll 3 " or "Emp 4" in minis_in_hand:
            return None  # Don't play anything until gold is sufficient
    return None  # No valid play

# Clicking logic for selecting a minion to play
def click_minion_and_map(selected_minion, minis_in_hand):
    if selected_minion:
        # Find the region where the selected minion is located
        selected_region = next(region for minion, region in zip(minis_in_hand, regions) if minion == selected_minion)

        # Click on the region where the minion is located
        region_center_x = selected_region[0] + selected_region[2] // 2
        region_center_y = selected_region[1] + selected_region[3] // 2
        pyautogui.click(region_center_x, region_center_y)

        # Now click on one of the three predefined map positions
        map_positions = [(1475, 945), (1265, 778), (1037, 940)]
        selected_map_pos = random.choice(map_positions)
        pyautogui.click(selected_map_pos)
    else:
        print("No valid minion to play.")

# GUI with Tkinter
class BotGUI(tk.Tk):
    def __init__(self):
        super().__init__()
        self.title("Rumble Bot")
        self.geometry("600x400")
        self.is_running = False

        # Textbox to display log output
        self.log_output = tk.Text(self, wrap=tk.WORD, height=15, width=60)
        self.log_output.pack(padx=10, pady=10)

        # Add a label for current hand and gold count
        self.current_hand_label = tk.Label(self, text="Current hand: ")
        self.current_hand_label.pack()

        self.current_gold_label = tk.Label(self, text="Current gold: ")
        self.current_gold_label.pack()

        # Start/Stop Button
        self.toggle_button = tk.Button(self, text="Start Bot", command=self.toggle_bot)
        self.toggle_button.pack(pady=10)

        # Bind the 'Q' key to start/stop bot
        self.bind("<q>", self.toggle_bot)

    def toggle_bot(self, event=None):
        self.is_running = not self.is_running
        if self.is_running:
            self.toggle_button.config(text="Stop Bot")
            self.start_bot()
        else:
            self.toggle_button.config(text="Start Bot")

    def start_bot(self):
        thread = Thread(target=self.run_bot)
        thread.start()

    def run_bot(self):
        try:
            while self.is_running:
                # Check if the "battle started" image exists to start the bot
                battle_started = find_image(
                    r"C:\Users\alanw\Documents\GitHub\Class\Automation tools\Reference folders\Rumble pvp menu management\region_910x1349_87x61 battle started.png")
                if battle_started:
                    self.log_output.insert(tk.END, "Battle Started\n")
                    self.log_output.yview(tk.END)

                    # Run the bot during the battle
                    while self.is_running:
                        gold_count = count_gold()
                        minis_in_hand = check_images_in_regions(image_paths, regions)
                        selected_minion = select_best_play(minis_in_hand, gold_count)

                        if selected_minion:
                            self.log_output.insert(tk.END, f"Selected play: {selected_minion}\n")
                            self.log_output.yview(tk.END)

                        click_minion_and_map(selected_minion, minis_in_hand)
                        time.sleep(2)  # Adjust time as needed

                        # Check for "battle ended" every 10 seconds
                        battle_ended = None
                        for _ in range(10):
                            battle_ended = find_image(
                                r"C:\Users\alanw\Documents\GitHub\Class\Automation tools\Reference folders\Rumble pvp menu management\region_1151x1276_242x67 battle ended.png")
                            if battle_ended:
                                break
                            time.sleep(1)  # Wait for 1 second before checking again

                        if battle_ended:
                            self.log_output.insert(tk.END, "Battle Ended\n")
                            self.log_output.yview(tk.END)
                            self.is_running = False  # Stop bot after the battle ends

        except Exception as e:
            self.log_output.insert(tk.END, f"Error: {str(e)}\n")
            self.log_output.yview(tk.END)


def find_image(image_path, confidence=0.9):
    try:
        result = pyautogui.locateOnScreen(image_path, confidence=confidence)
        if result:
            return True
        return False
    except Exception as e:
        return False



# Run the application
if __name__ == "__main__":
    app = BotGUI()
    app.mainloop()
