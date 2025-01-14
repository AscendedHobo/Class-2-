import tkinter as tk
import pyautogui
import threading
import time
from pynput import keyboard

# Coordinates and RGB values for Spell Readiness and Casting
SPELL_READY_COORDINATES = (17, 1399)
SPELL_READY_RGB = (255, 0, 0)
DEFENSIVE_COORDINATES = (1264, 189)
DEFENSIVE_ABILITIES = {
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

# Control flags
running = False
key_held = False
last_activation = {"obsidian_scales": 0}


def handle_defensive_skills():
    """Handles automatic defensive abilities."""
    global running, last_activation
    while running:
        current_color = pyautogui.screenshot().getpixel(DEFENSIVE_COORDINATES)

        for ability, data in DEFENSIVE_ABILITIES.items():
            if current_color == data["rgb"]:
                if ability == "obsidian_scales":
                    current_time = time.time()
                    if current_time - last_activation.get(ability, 0) < data.get("cooldown", 0):
                        continue
                    last_activation[ability] = current_time

                if isinstance(data["keypress"], list):
                    pyautogui.hotkey(*data["keypress"])
                else:
                    pyautogui.press(data["keypress"])
                time.sleep(0.3)  # Avoid spamming
                break

        time.sleep(0.1)


def handle_disintegrate():
    """Handles Disintegrate cast automation."""
    global running
    while running:
        current_spell_ready_color = pyautogui.screenshot().getpixel(SPELL_READY_COORDINATES)
        if current_spell_ready_color == SPELL_READY_RGB:
            pyautogui.press("num5")
            time.sleep(0.3)  # Avoid spamming

        time.sleep(0.1)


def toggle_program():
    """Toggles the automation program on and off."""
    global running
    if running:
        running = False
        toggle_button.config(text="Start")
        print("Program stopped.")
    else:
        running = True
        toggle_button.config(text="Stop")
        print("Program started.")
        threading.Thread(target=handle_defensive_skills, daemon=True).start()
        threading.Thread(target=handle_disintegrate, daemon=True).start()


# Create a simple tkinter UI
def create_ui():
    global toggle_button

    root = tk.Tk()
    root.title("Evoker Automation")

    toggle_button = tk.Button(root, text="Start", command=toggle_program, width=10, height=2)
    toggle_button.pack(pady=10)

    root.mainloop()


if __name__ == "__main__":
    # Start the UI
    create_ui()
