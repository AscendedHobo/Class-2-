import pyautogui
import time
import pyperclip
import re
import threading
from tkinter import Tk, Button
from pynput import keyboard
from PIL import Image, ImageEnhance, ImageOps
import pytesseract

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

    # Remove the last line (usually "XXXX Copper")
    if filtered_lines:
        filtered_lines = filtered_lines[:-1]

    # Include the NPC name at the start, if available
    if npc_name:
        filtered_lines.insert(0, npc_name)

    return "\n".join(filtered_lines)

# Function to extract text from the screen region using OCR with preprocessing
def extract_text_from_region(region):
    print("Taking screenshot of the region...")
    screenshot = pyautogui.screenshot(region=region)

    print("Preprocessing the screenshot...")
    # Convert to grayscale
    grayscale = screenshot.convert("L")
    # Increase contrast
    enhancer = ImageEnhance.Contrast(grayscale)
    enhanced_image = enhancer.enhance(2.0)
    # Apply a threshold filter
    processed_image = ImageOps.autocontrast(enhanced_image)

    print("Performing OCR on the preprocessed screenshot...")
    text = pytesseract.image_to_string(processed_image, lang='eng')
    return text

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
    text_region = (1584, 341, 664, 654)  # Region of the screen containing the text
    button_region = (1004, 1082, 89, 76)  # Region of the screen containing the button
    reference_image_path = "path_to_read_aloud_button_image.png"  # Replace with your image path

    while running:
        print("Waiting for Alt Gr key press...")
        alt_gr_pressed.wait()  # Wait for Alt Gr key to start
        alt_gr_pressed.clear()

        print("Alt Gr pressed. Starting execution...")

        # Extract text from the screen region
        raw_text = extract_text_from_region(text_region)

        # Filter the text
        print("Filtering text...")
        filtered_text = filter_text(raw_text)

        # Copy the filtered text to the clipboard
        print("Copying filtered text to clipboard...")
        pyperclip.copy(filtered_text)

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
        while not is_image_displayed(button_region, reference_image_path):
            print("Read aloud button not found. Retrying...")
            time.sleep(0.5)  # Retry interval

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
