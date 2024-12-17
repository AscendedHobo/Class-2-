import pyautogui
import time
import random
import keyboard  # For global key detection
import tkinter as tk
from tkinter import scrolledtext

# Global variables
running = False  # State of the bot
root = None  # Reference to the Tkinter window

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
    minis_in_hand = []
    for region in regions:
        for image_path in image_paths:
            try:
                result = pyautogui.locateOnScreen(image_path, region=region, confidence=0.9)
                if result:
                    minion_name = image_path.split("\\")[-1].replace(".png", "")
                    minis_in_hand.append(minion_name)
                    break
            except Exception:
                pass
    return minis_in_hand

# Play selection logic
def select_best_play(minis_in_hand, gold_count):
    if gold_count >= 4 and "Emp 4" in minis_in_hand:
        return "Emp 4"
    if gold_count >= 5:
        if "Ranger 5" in minis_in_hand:
            return "Ranger 5"
        elif "Troll 3" in minis_in_hand:
            return "Troll 3"
    if gold_count >= 7:
        return sorted(minis_in_hand, key=lambda x: int(x.split()[-1]))[0] if minis_in_hand else None
    return None

def click_minion_and_map(selected_minion, minis_in_hand):
    if selected_minion:
        selected_region = next(region for minion, region in zip(minis_in_hand, regions) if minion == selected_minion)
        region_center_x = selected_region[0] + selected_region[2] // 2
        region_center_y = selected_region[1] + selected_region[3] // 2
        pyautogui.click(region_center_x, region_center_y)

        map_positions = [(1475, 945), (1265, 778), (1037, 940)]
        pyautogui.click(random.choice(map_positions))

# Main bot function
def run_bot(log_area):
    global running
    while running:
        gold_count = count_gold()
        minis_in_hand = check_images_in_regions(image_paths, regions)
        selected_minion = select_best_play(minis_in_hand, gold_count)

        log_area.insert(tk.END, f"Gold: {gold_count}, Hand: {minis_in_hand}, Play: {selected_minion}\n")
        log_area.see(tk.END)

        click_minion_and_map(selected_minion, minis_in_hand)
        time.sleep(2)

# Start/Pause logic
def toggle_bot(log_area):
    global running
    running = not running
    if running:
        log_area.insert(tk.END, "Bot started.\n")
        run_bot(log_area)
    else:
        log_area.insert(tk.END, "Bot paused.\n")

# GUI Setup
def create_gui():
    global root
    root = tk.Tk()
    root.title("Bot Control")

    log_area = scrolledtext.ScrolledText(root, width=60, height=20)
    log_area.pack()

    root.after(100, keyboard.on_press_key, "q", lambda _: toggle_bot(log_area))
    root.mainloop()

# Run GUI
if __name__ == "__main__":
    create_gui()
