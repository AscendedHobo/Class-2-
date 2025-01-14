import pyautogui
import time
import pyperclip
import re
import threading
from tkinter import Tk, Button
from pynput import keyboard
from PIL import Image

# Function to filter text
def filter_text(raw_text):
    lines = raw_text.splitlines()
    filtered_lines = []
    skip_section = False
    npc_name = None

    for line in lines:
        # Capture NPC name if present and remove the number
        if line.startswith("[NPC:"):
            npc_name = re.sub(r"\[NPC:\s*\d+\]\s*", "", line)
            continue
        # Start skipping lines after "Objectives" is encountered
        if "Objectives" in line:
            skip_section = True
            continue
        # Stop skipping lines after "Rewards" is encountered
        if "Rewards" in line:
            skip_section = False
            continue
        # Skip lines within the "Objectives" to "Rewards" block
        if skip_section:
            continue
        # Skip currency lines like "[CurrencyID: 3008] Valorstones 10"
        if re.match(r"\[CurrencyID:\s*\d+\]\s*.*", line):
            continue
        # Add lines outside the block and not matching Quest prefixes
        if not line.startswith("[Quest:"):
            filtered_lines.append(line)

    # Remove the last line if it matches the format "XXXX Copper"
    if filtered_lines and re.match(r"^\d+\s+Copper$", filtered_lines[-1]):
        filtered_lines = filtered_lines[:-1]

    # Include the NPC name at the start, if available
    if npc_name:
        filtered_lines.insert(0, npc_name)

    return "\n".join(filtered_lines)

# Function to check if the target image is displayed
def is_image_displayed(region, reference_image_path, confidence=0.7):
    try:
        print("Checking for image display...")
        result = pyautogui.locateOnScreen(reference_image_path, region=region, confidence=confidence)
        if result:
            print("Image match found.")
            return True
        print("Image match not found.")
        return False
    except Exception as e:
        print(f"Error checking image: {e}")
        return False

# Program execution
running = False
alt_gr_pressed = threading.Event()

# Listener for Alt Gr key
def on_press(key):
    try:
        if key == keyboard.Key.alt_gr:
            alt_gr_pressed.set()
    except AttributeError:
        pass

def start_program():
    global running
    running = True
    threading.Thread(target=main_loop).start()

    # Start listener
    listener = keyboard.Listener(on_press=on_press)
    listener.start()

def stop_program():
    global running
    running = False
    alt_gr_pressed.set()  # Ensure any waiting threads proceed

    # Stop the listener
    for thread in threading.enumerate():
        if isinstance(thread, keyboard.Listener):
            thread.stop()

def main_loop():
    global running
    reference_image_path = "C:\\Users\\alanw\\Desktop\\temp region dump\\region_1021x1089_41x38.png"
    region = (1004, 1082, 89, 76)

    while running:
        print("Waiting for Alt Gr key press...")
        alt_gr_pressed.wait()  # Wait for Alt Gr key to start
        alt_gr_pressed.clear()

        print("Alt Gr pressed. Starting execution...")

        # Step 1: Click at the initial position to copy text
        print("Clicking initial position...")
        pyautogui.click(x=2261, y=315)
        time.sleep(0.5)

        # Step 2: Click at the position in the new window
        print("Clicking in new window...")
        pyautogui.doubleClick(x=905, y=308)
        time.sleep(.3)

        pyautogui.click(x=905, y=308)
        time.sleep(.5)

        # Select all and copy text using key down and up
        print("Selecting and copying text...")
        pyautogui.keyDown('ctrl')
        time.sleep(0.2)
        pyautogui.press('a')
        time.sleep(0.2)
        pyautogui.keyUp('ctrl')
        time.sleep(0.2)
        pyautogui.keyDown('ctrl')
        time.sleep(0.2)
        pyautogui.press('c')
        time.sleep(0.2)
        pyautogui.keyUp('ctrl')
        time.sleep(0.2)

        # Retrieve the copied text from the clipboard
        print("Retrieving copied text...")
        raw_text = pyperclip.paste()

        # Filter the text
        print("Filtering text...")
        filtered_text = filter_text(raw_text)

        # Copy the filtered text back to the clipboard
        print("Copying filtered text to clipboard...")
        pyperclip.copy(filtered_text)

        # Press Escape to close the window
        print("Pressing Escape to close the window...")
        pyautogui.press('esc')
        time.sleep(0.5)

        # Alt-Tab to switch to chat application using key down and up
        print("Switching to chat application...")
        pyautogui.keyDown('alt')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        time.sleep(0.5)

        # Click to select the chat box
        print("Selecting chat box...")
        pyautogui.click(x=1407, y=1243)

        # Paste the text into the chat box
        print("Pasting text into chat box...")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(2)

        # Check if the read aloud button is visible
        print("Checking for read aloud button...")
        while not is_image_displayed(region, reference_image_path):
            print("Read aloud button not found. Retrying...")
            time.sleep(0.5)  # Retry interval

                # Scroll down one 'click' with the mouse wheel
        print("Scrolling down one 'click'...")
        pyautogui.scroll(-1)  # Use a negative value to scroll down
        time.sleep(0.5)  # Small delay after scrolling


        print("Read aloud button found. Clicking...")
        pyautogui.click(x=1044, y=1110)
        time.sleep(1)

        # Alt-Tab back to the game using key down and up
        print("Switching back to game...")
        pyautogui.keyDown('alt')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        time.sleep(0.5)

        # End cycle here and wait for the next Alt Gr press
        print("Cycle complete. Waiting for next Alt Gr press...")

# GUI setup
root = Tk()
root.title("Voice Automation")

start_button = Button(root, text="Start", command=start_program, width=20)
start_button.pack(pady=10)

stop_button = Button(root, text="Stop", command=stop_program, width=20)
stop_button.pack(pady=10)

root.mainloop()
