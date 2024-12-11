import pyautogui
import time

def find_color(target_color, region=None):
    """
    Scans a region of the screen for a pixel with the target color.
    Returns the pixel's position or None if not found.
    """
    screenshot = pyautogui.screenshot(region=region) if region else pyautogui.screenshot()
    width, height = screenshot.size
    
    for x in range(width):
        for y in range(height):
            if screenshot.getpixel((x, y))[:3] == target_color:
                return x + (region[0] if region else 0), y + (region[1] if region else 0)
    return None

# Define colors (using the RGB values you've given)
blue_color = (34, 108, 167)   # Example blue color
green_color = (30, 151, 80)  # Example green color

# Define the region to search for the colors (adjust the width and height as needed)
region = (630, 414, 100, 100)  # Example region (x, y, width, height)

# Searching for the blue area to click
print("Searching for the blue area...")
blue_position = None
while not blue_position:
    blue_position = find_color(blue_color, region=region)
    time.sleep(0.0001)  # Avoid overloading CPU

print(f"Blue area found at {blue_position}, clicking...")
pyautogui.click(blue_position)

# Waiting for the green area to appear
print("Waiting for green...")
green_position = None
while not green_position:
    green_position = find_color(green_color, region=region)
    time.sleep(0.0001)  # Faster polling for green

print(f"Green area found at {green_position}, clicking...")
pyautogui.click(green_position)
print("Reaction test complete!")
