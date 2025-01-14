import tkinter as tk
import pyautogui
import threading
import time

# Coordinates and RGB values
SPELL_READY_COORDINATES = (17, 1399)
SPELL_READY_RGB = (255, 0, 0)

# Control flag
running = False

def press_key_if_ready():
    """Continuously checks if Spell 5 is ready and presses 'num5'."""
    global running
    while running:
        # Check the RGB color at the specified screen coordinates for spell readiness
        current_spell_ready_color = pyautogui.screenshot().getpixel(SPELL_READY_COORDINATES)
        print(f"Current RGB at {SPELL_READY_COORDINATES}: {current_spell_ready_color}")  # Trace RGB value

        if current_spell_ready_color == SPELL_READY_RGB:
            print("Spell 5 ready! Pressing 'num5'")
            pyautogui.press("num5")
            time.sleep(0.3)  # Avoid spamming
        else:
            print("Spell 5 not ready.")  # Trace when condition isn't met

        time.sleep(0.1)  # Polling interval

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
        threading.Thread(target=press_key_if_ready, daemon=True).start()

# Create a simple tkinter UI
def create_ui():
    global toggle_button

    root = tk.Tk()
    root.title("Spell Automation")

    toggle_button = tk.Button(root, text="Start", command=toggle_program, width=10, height=2)
    toggle_button.pack(pady=10)

    root.mainloop()

if __name__ == "__main__":
    # Start the UI
    create_ui()
