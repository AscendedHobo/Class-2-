import pyautogui
import time
import pyperclip
import re
import threading
from tkinter import Tk, Button
from pynput import keyboard

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
        # Add lines outside the block and not matching Quest prefixes
        if not line.startswith("[Quest:"):
            filtered_lines.append(line)

   # Remove the last line only if it matches the pattern of an integer followed by "Copper"
    if filtered_lines and re.match(r"^\d+\\s+Copper$", filtered_lines[-1]):
        filtered_lines = filtered_lines[:-1]


    # Include the NPC name at the start, if available
    if npc_name:
        filtered_lines.insert(0, npc_name)

    return "\n".join(filtered_lines)

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

    while running:
        alt_gr_pressed.wait()  # Wait for Alt Gr key to start
        alt_gr_pressed.clear()

        # Step 1: Click at the initial position to copy text
        pyautogui.click(x=2261, y=315)
        time.sleep(0.5)

        # Step 2: Click at the position in the new window
        pyautogui.doubleClick(x=905, y=308)
        time.sleep(.3)

        pyautogui.click(x=905, y=308)
        time.sleep(.5)


        # Select all and copy text using key down and up
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        pyautogui.press('a')
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)
        pyautogui.keyDown('ctrl')
        time.sleep(0.1)
        pyautogui.press('c')
        time.sleep(0.1)
        pyautogui.keyUp('ctrl')
        time.sleep(0.1)

        # Retrieve the copied text from the clipboard
        raw_text = pyperclip.paste()

        # Filter the text
        filtered_text = filter_text(raw_text)

        # Copy the filtered text back to the clipboard
        pyperclip.copy(filtered_text)

        # Press Escape to close the window
        pyautogui.press('esc')
        time.sleep(0.5)

        # Alt-Tab to switch to chat application
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.5)

        # Click to select the chat box
        pyautogui.click(x=1407, y=1243)

        # Paste the text into the chat box
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)

        pyautogui.press('enter')
        time.sleep(3)

        # Click to start voice response
        pyautogui.click(x=1867, y=1293)
        time.sleep(1)

        # Alt-Tab back to the game
        pyautogui.hotkey('alt', 'tab')

        # Wait for the voice to finish (Alt Gr key pressed again)
        alt_gr_pressed.wait()
        alt_gr_pressed.clear()

        # Alt-Tab back to the webpage
        # Alt-Tab to switch to chat application using key down and up
        pyautogui.keyDown('alt')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        time.sleep(2)

        # Click to close the voice chat
        pyautogui.click(x=1331, y=1289)
        time.sleep(0.5)

        # Alt-Tab back to the game
        pyautogui.hotkey('alt', 'tab')
        time.sleep(0.5)

# GUI setup
root = Tk()
root.title("Voice Automation")

start_button = Button(root, text="Start", command=start_program, width=20)
start_button.pack(pady=10)

stop_button = Button(root, text="Stop", command=stop_program, width=20)
stop_button.pack(pady=10)

root.mainloop()
