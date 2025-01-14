import tkinter as tk
import pyautogui
import threading
import time

# Coordinates and RGB values for abilities
ABILITY_COORDINATES = (1264, 189)
ABILITIES = {
    "renewing_blaze": {
        "rgb": (91, 10, 23),
        "keypress": "3"
    },
    "obsidian_scales": {
        "rgb": (102, 85, 77),
        "keypress": ["shift", "3"],
        "cooldown": 12  # Cooldown duration in seconds
    },
    "zephyr": {
        "rgb": (139, 81, 66),
        "keypress": ["alt", "3"]
    }
}

# Control flag for the program
running = False
# Track the last activation time for abilities
last_activation = {"obsidian_scales": 0}

def press_key_with_delay(keys):
    """Press keys with a delay between modifier and main key."""
    if isinstance(keys, list):
        modifier, main_key = keys
        print(f"Holding {modifier} and pressing {main_key}")
        pyautogui.keyDown(modifier)
        time.sleep(0.3)  # Wait before pressing the main key
        pyautogui.press(main_key)
        time.sleep(0.3)  # Ensure keypress is registered
        pyautogui.keyUp(modifier)
        print(f"Released {modifier}")
    else:
        print(f"Pressing {keys}")
        pyautogui.press(keys)
        time.sleep(0.3)

def check_and_press():
    global running
    while running:
        # Get the RGB color at the specified screen coordinates
        current_color = pyautogui.screenshot().getpixel(ABILITY_COORDINATES)

        for ability, data in ABILITIES.items():
            if current_color == data["rgb"]:
                if ability == "obsidian_scales":
                    # Check cooldown for obsidian scales
                    current_time = time.time()
                    if current_time - last_activation.get(ability, 0) < data.get("cooldown", 0):
                        print(f"{ability} is on cooldown.")
                        continue
                    last_activation[ability] = current_time

                print(f"Activating {ability}")
                press_key_with_delay(data["keypress"])
                break

        time.sleep(0.1)  # Polling interval

def toggle_program():
    global running
    if running:
        running = False
        toggle_button.config(text="Start")
        print("Program stopped.")
    else:
        running = True
        toggle_button.config(text="Stop")
        print("Program started.")
        threading.Thread(target=check_and_press, daemon=True).start()

# Create a simple tkinter UI
def create_ui():
    global toggle_button

    root = tk.Tk()
    root.title("Evoker RGB Tracker")

    toggle_button = tk.Button(root, text="Start", command=toggle_program, width=10, height=2)
    toggle_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    create_ui()
