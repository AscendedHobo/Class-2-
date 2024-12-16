import pyautogui
import time
from PIL import Image, ImageChops
import os

def regions():
    return {
        "Section 1": [(1125, 1331), (1145, 1361)],
        "Section 2": [(1275, 1330), (1297, 1360)],
        "Section 3": [(1427, 1331), (1453, 1359)],
        "Section 4": [(1580, 1330), (1606, 1357)],
    }

def capture_region(region, section, screenshot_count):
    left, top = region[0]
    right, bottom = region[1]
    width, height = right - left, bottom - top
    return pyautogui.screenshot(region=(left, top, width, height))

def is_duplicate(new_image, section):
    section_dir = f"screenshots/{section}"
    if not os.path.exists(section_dir):
        return False

    for file in os.listdir(section_dir):
        existing_image = Image.open(os.path.join(section_dir, file))
        if ImageChops.difference(new_image, existing_image).getbbox() is None:
            return True

    return False

def save_image(image, section, screenshot_count):
    section_dir = f"screenshots/{section}"
    os.makedirs(section_dir, exist_ok=True)
    filename = f"{section} x screenshot {screenshot_count}.png"
    image.save(os.path.join(section_dir, filename))

def main():
    screenshot_count = {section: 1 for section in regions()}
    
    while True:
        for section, region in regions().items():
            screenshot = capture_region(region, section, screenshot_count[section])
            if not is_duplicate(screenshot, section):
                save_image(screenshot, section, screenshot_count[section])
                screenshot_count[section] += 1
        time.sleep(5)

if __name__ == "__main__":
    main()
