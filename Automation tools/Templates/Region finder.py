import pyautogui
import time
import os
from PIL import Image


print("Hover over the top-left corner of the region and press Enter...")
input()  # Wait for user to hover over the top-left corner
top_left = pyautogui.position()
print(f"Top-left corner: {top_left}")

print("Hover over the bottom-right corner of the region and press Enter...")
input()  # Wait for user to hover over the bottom-right corner
bottom_right = pyautogui.position()
print(f"Bottom-right corner: {bottom_right}")

# Calculate region
x1, y1 = top_left
x2, y2 = bottom_right
region = (x1, y1, x2 - x1, y2 - y1)
print(f"Region: {region}")

########################################################################################################
# same =  True
# 
# = True:

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


