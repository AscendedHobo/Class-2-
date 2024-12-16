import pyautogui
import time
import os
from PIL import Image


userchoice = input(("Shots to be taken : "))

userchoice = int(userchoice)+1

region=(172, 451, 286, 254)

screenshot_paths = []
screenshots = []  # Store screenshots in a list for easy comparison
for i in range(1, userchoice):  # Loop to take 3 screenshots
    screenshot = pyautogui.screenshot(region=region)
    screenshots.append(screenshot)

    file_path = os.path.join("C:/Users/alanw/Documents/GitHub/Class/Automation tools/Templates/", f"screenshot_{i}.png")  # Save in the same directory as the script
    screenshot.save(file_path)

    screenshot_paths.append(file_path)
    print(f"Screenshot {i} saved to {file_path}")
    time.sleep(3)  # Wait 5 seconds between captures

########################################################################################################
# comparing screenshots

from PIL import Image

for i in range(1, userchoice):
    # Load the images
    screen1_path = f"C:\\Users\\alanw\\Documents\\GitHub\\Class\\Automation tools\\Templates\\screenshot_{i}.png"
    screen2_path = f"C:\\Users\\alanw\\Documents\\GitHub\\Class\\Automation tools\\Templates\\screenshot_{i+1}.png"

    screen1 = Image.open(screen1_path)
    screen2 = Image.open(screen2_path)

    # Compare the images
    if list(screen1.getdata()) == list(screen2.getdata()):
        print(f"{i} and {i+1} are the same")
    else:
        print(f"{i} and {i+1} are different")






