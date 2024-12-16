import pyautogui
from PIL import ImageGrab

# Specify the target pixel position and expected RGB value
target_x, target_y = 2514, 1239
expected_rgb = (145, 86, 36)

# Define the click position
click_x, click_y = 1928, 1310

# Capture the screen and get the RGB value at the target position
screenshot = ImageGrab.grab()
current_rgb = screenshot.getpixel((target_x, target_y))

# Check if the RGB value matches the expected value
if current_rgb == expected_rgb:
    print(f"Match found at ({target_x}, {target_y}). RGB: {current_rgb}")
    # Move to the click position and perform a left-click
    pyautogui.moveTo(click_x, click_y)
    pyautogui.click()
else:
    print(f"No match. RGB at ({target_x}, {target_y}) is {current_rgb}")
