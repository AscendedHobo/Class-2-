import pyautogui
import time
import random
from PIL import Image, ImageChops
import os

# Define your regions (these are the same regions from your previous code)
def regions():
    return {
        "Section 1": [(1125, 1331), (1145, 1361)],
        "Section 2": [(1275, 1330), (1297, 1360)],
        "Section 3": [(1427, 1331), (1453, 1359)],
        "Section 4": [(1580, 1330), (1606, 1357)],
    }

# Define the possible placement points
placement_points = [
    (1119, 942),  # Left of tower
    (1384, 947),  # Right of tower
    (1247, 795),  # Ahead of tower
]

# Define the folder paths for reference images
reference_paths = {
    "Section 1": "C:/Users/alanw/Desktop/screenshots/Section 1/",
    "Section 2": "C:/Users/alanw/Desktop/screenshots/Section 2/",
    "Section 3": "C:/Users/alanw/Desktop/screenshots/Section 3/",
    "Section 4": "C:/Users/alanw/Desktop/screenshots/Section 4/",
}

def capture_region(region):
    left, top = region[0]
    right, bottom = region[1]
    width, height = right - left, bottom - top
    return pyautogui.screenshot(region=(left, top, width, height))

def is_duplicate(new_image, section):
    section_dir = reference_paths[section]
    for file in os.listdir(section_dir):
        if file.endswith(".png"):  # Only check PNG files
            existing_image = Image.open(os.path.join(section_dir, file))
            if ImageChops.difference(new_image, existing_image).getbbox() is None:
                return True
    return False

def find_lowest_cost_image():
    cost_images = []

    # Iterate over all sections and find the lowest cost image
    for section in regions():
        for file in os.listdir(reference_paths[section]):
            if file.endswith(".png"):
                try:
                    cost = int(file.split()[1])  # Extract the number from filename (e.g., "1 1.png" -> 1)
                    cost_images.append((cost, section, file))
                except ValueError:
                    continue
    
    cost_images.sort(key=lambda x: x[0])  # Sort by cost (lowest first)

    return cost_images[0] if cost_images else None

def click_on_image(image, section):
    # Find the center of the region to click
    region = regions()[section]
    left, top = region[0]
    right, bottom = region[1]
    width, height = right - left, bottom - top
    center_x = left + width // 2
    center_y = top + height // 2
    
    pyautogui.click(center_x, center_y)  # Click on the center

def click_random_placement():
    # Click on one of the random placement points
    random_point = random.choice(placement_points)
    pyautogui.click(random_point[0], random_point[1])

def main():
    while True:
        # Capture the current region and check for the lowest cost image
        lowest_cost_image = find_lowest_cost_image()
        
        if lowest_cost_image:
            cost, section, image_file = lowest_cost_image
            screenshot = capture_region(regions()[section])

            # Perform the click sequence for the lowest cost monster
            click_on_image(screenshot, section)
            time.sleep(0.8)  # Wait for 0.8 seconds before the second click
            click_random_placement()

        else:
            # If no valid image found, wait for the animation to change
            time.sleep(1.5)

        time.sleep(5)  # Wait 5 seconds before checking again

if __name__ == "__main__":
    main()
