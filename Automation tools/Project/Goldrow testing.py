import easyocr
from PIL import Image
import pyautogui

# Define the region (adjust as needed)
region = (1090, 1302, 75, 74)

# Capture the screenshot
screenshot = pyautogui.screenshot(region=region)

# Convert the screenshot to grayscale (optional, can help in some cases)
screenshot_gray = screenshot.convert('L')

# Initialize EasyOCR reader
reader = easyocr.Reader(['en'])

# Use EasyOCR to extract text from the screenshot
result = reader.readtext(screenshot_gray)

# Print the results
for detection in result:
    print(detection[1])  # The OCR result is in detection[1]
