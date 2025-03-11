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

    # Include the NPC name at the start, if available
    if npc_name:
        filtered_lines.insert(0, npc_name)

    return "\n".join(filtered_lines)

# Function to extract text from the screen region using OCR with preprocessing
def extract_text_from_region(region):
    print("Taking screenshot of the region...")
    screenshot = pyautogui.screenshot(region=region)

    print("Preprocessing the screenshot...")
    grayscale = screenshot.convert("L")
    enhancer = ImageEnhance.Contrast(grayscale)
    enhanced_image = enhancer.enhance(2.0)
    processed_image = ImageOps.autocontrast(enhanced_image)

    print("Performing OCR on the preprocessed screenshot...")
    text = pytesseract.image_to_string(processed_image, lang='eng')
    return text

# Function to check if the target image is displayed in the region (excluding the lowest 5% of the screen)
def is_image_displayed(reference_image_path, confidence=0.7):
    try:
        print("Checking for image in specified screen region...")
        screen_width, screen_height = pyautogui.size()
        # Exclude the top 20% and the bottom 5% of the screen
        region = (0, int(screen_height * 0.2), screen_width, int(screen_height * 0.75))
        screenshot = pyautogui.screenshot(region=region)
        result = pyautogui.locate(reference_image_path, screenshot, confidence=confidence)
        
        if result:
            time.sleep(0.3)
            print("Image match found.")
            x, y, width, height = result
            screen_x = x + region[0]
            screen_y = y + region[1]
            center_x = screen_x + width // 2
            center_y = screen_y + height // 2
            return True, (center_x, center_y)
        
        print("Image match not found.")
        return False, None
    except Exception as e:
        print(f"Error checking image: {e}")
        return False, None

# Global variables for program execution
running = False
alt_gr_pressed = threading.Event()
shift_alt_gr_pressed = threading.Event()
pressed_keys = set()  # Track currently pressed keys

# Listener for key press and release to detect Alt Gr and Shift + Alt Gr combinations
def on_press(key):
    global alt_gr_pressed, shift_alt_gr_pressed, pressed_keys
    pressed_keys.add(key)
    try:
        if key == keyboard.Key.alt_gr:
            # Check if either shift key is currently held down
            if keyboard.Key.shift in pressed_keys or keyboard.Key.shift_r in pressed_keys:
                shift_alt_gr_pressed.set()
            else:
                alt_gr_pressed.set()
    except AttributeError:
        pass

def on_release(key):
    global pressed_keys
    if key in pressed_keys:
        pressed_keys.remove(key)

def start_program():
    global running
    running = True
    threading.Thread(target=main_loop).start()
    listener = keyboard.Listener(on_press=on_press, on_release=on_release)
    listener.start()

def stop_program():
    global running
    running = False
    alt_gr_pressed.set()
    shift_alt_gr_pressed.set()
    for thread in threading.enumerate():
        if isinstance(thread, keyboard.Listener):
            thread.stop()

def main_loop():
    global running
    text_region = (1584, 341, 664, 654)  # Screen region containing the text
    reference_image_path = "C:\\Users\\alanw\\Desktop\\temp region dump\\region_1021x1089_41x38.png"  # Update with your image path
    shift_mode = False

    while running:
        print("Waiting for Alt Gr key press...")
        if shift_alt_gr_pressed.wait(0.1):
            pass

        alt_gr_pressed.wait()
        alt_gr_pressed.clear()
        print("Alt Gr pressed. Starting execution...")

        raw_text = extract_text_from_region(text_region)
        print("Filtering text...")
        filtered_text = filter_text(raw_text)
        print("Copying filtered text to clipboard...")
        pyperclip.copy(filtered_text)

        print("Switching to chat application...")
        pyautogui.keyDown('alt')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        time.sleep(0.5)

        if shift_alt_gr_pressed.is_set():
            print("Shift + Alt Gr detected. Switching voice tab...")
            pyautogui.hotkey('ctrl', 'tab')
            time.sleep(0.5)
            shift_mode = True
            shift_alt_gr_pressed.clear()

        print("Selecting chat box...")
        pyautogui.click(x=1407, y=1243)
        print("Pasting text into chat box...")
        pyautogui.hotkey('ctrl', 'v')
        time.sleep(0.5)
        pyautogui.press('enter')
        time.sleep(4)

        print("Checking for read aloud button...")
        found = False
        while not found:
            found, center_coords = is_image_displayed(reference_image_path)
            if not found:
                print("Read aloud button not found. Retrying...")
                time.sleep(0.5)

        # Retry click logic: recapture screenshot and locate image before each click attempt
        for attempt in range(3):
            found, coords = is_image_displayed(reference_image_path)
            if found:
                print(f"Attempt {attempt + 1}: Found button at {coords}. Clicking...")
                pyautogui.click(coords[0], coords[1])
                time.sleep(0.2)
                pyautogui.moveTo(500, 500)  # Move cursor away
                time.sleep(0.5)
                still_found, _ = is_image_displayed(reference_image_path)
                if not still_found:
                    print("Button click succeeded.")
                    break
                else:
                    print(f"Click attempt {attempt + 1} failed. Retrying...")
            else:
                print(f"Attempt {attempt + 1}: Button not found. Retrying...")
                time.sleep(0.5)
        else:
            print("Failed to click the button after 3 attempts.")

        if shift_mode:
            print("Switching back to default voice tab...")
            pyautogui.hotkey('ctrl', 'shift', 'tab')
            time.sleep(0.5)
            shift_mode = False

        print("Switching back to game...")
        pyautogui.keyDown('alt')
        time.sleep(0.2)
        pyautogui.press('tab')
        time.sleep(0.2)
        pyautogui.keyUp('alt')
        time.sleep(0.5)

        print("Cycle complete. Waiting for next Alt Gr press...")

# GUI setup
root = Tk()
root.title("Voice Automation")
start_button = Button(root, text="Start", command=start_program, width=20)
start_button.pack(pady=10)
stop_button = Button(root, text="Stop", command=stop_program, width=20)
stop_button.pack(pady=10)
root.mainloop()
