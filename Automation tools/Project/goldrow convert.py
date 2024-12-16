from PIL import Image
import pytesseract
import pyautogui

# Step 1: Define the region coordinates (left, top, width, height)
# region = (1068, 1309, 577, 52)  # Replace with the region of your screenshot
# region = (1100, 1308, 516, 62)
region = (1090, 1302, 75, 74)


# Step 2: Capture the screen region
screenshot = pyautogui.screenshot(region=region)

# Step 3: Save or process the image (optional, for debugging)
screenshot.save("gold_row.png")

# Step 4: Use pytesseract to extract text
# Ensure Tesseract-OCR is installed on your system and is in the PATH
pytesseract.pytesseract.tesseract_cmd = r'C:\Program Files\Tesseract-OCR\tesseract.exe'  # Adjust for your OS
text = pytesseract.image_to_string(screenshot, config="--psm 7 digits")

# Step 5: Process the extracted text
# Assuming the numbers will always be in the gold sections
numbers = [int(num) for num in text.split() if num.isdigit()]

print(numbers)