import pyautogui
from PIL import ImageGrab

# Get the current mouse position
mouse_x, mouse_y = pyautogui.position()

# Capture the entire screen (or specific regions if necessary)
screenshot = ImageGrab.grab()

# Get the RGB value at the current mouse position
rgb_value = screenshot.getpixel((mouse_x, mouse_y))

print(f"The RGB value at the mouse position ({mouse_x}, {mouse_y}) is {rgb_value}")
