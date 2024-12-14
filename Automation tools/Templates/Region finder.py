import pyautogui
import time
import os
from PIL import Image


# print("Hover over the top-left corner of the region and press Enter...")
# input()  # Wait for user to hover over the top-left corner
# top_left = pyautogui.position()
# print(f"Top-left corner: {top_left}")

# print("Hover over the bottom-right corner of the region and press Enter...")
# input()  # Wait for user to hover over the bottom-right corner
# bottom_right = pyautogui.position()
# print(f"Bottom-right corner: {bottom_right}")

# # Calculate region
# x1, y1 = top_left
# x2, y2 = bottom_right
# region = (x1, y1, x2 - x1, y2 - y1)
# print(f"Region: {region}")


# same =  True
# while same == True:

#     screen1 = pyautogui.screenshot(region=(172, 451, 286, 254))
#     print("screen one taken")
#     time.sleep(5)
#     screen2 = pyautogui.screenshot(region=(172, 451, 286, 254))
#     print("screen two taken")

#     if screen1 == screen2:
        
#         print("Area is the same ")
#     else:
#         print("Change has been detected")
#         same = False


########################################################################################################


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
    time.sleep(5)  # Wait 5 seconds between captures

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








