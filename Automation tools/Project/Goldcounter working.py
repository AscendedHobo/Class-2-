import pyautogui
import time

# Reference RGB values for gold slots (within a reasonable tolerance range)
gold_refs = [
    (209, 186, 55), (208, 188, 65), (209, 190, 66), (239, 226, 84), 
    (251, 224, 82), (255, 232, 82), (254, 222, 75), (255, 233, 79), 
    (250, 225, 80), (255, 230, 74)
]

# Reference RGB value for "no gold"
no_gold_ref = (27, 27, 27)

# Positions of the gold slots
gold_positions = [
    (1129, 1402), (1188, 1396), (1253, 1395), (1301, 1400), 
    (1350, 1399), (1404, 1399), (1469, 1398), (1519, 1395), 
    (1577, 1395), (1630, 1401)
]

# Function to get RGB value from a position
def get_rgb_at_position(x, y):
    return pyautogui.screenshot(region=(x, y, 1, 1)).getpixel((0, 0))

# Function to determine if a color is close to the reference color
def is_gold_color(rgb, tolerance=30):
    for ref in gold_refs:
        if all(abs(rgb[i] - ref[i]) <= tolerance for i in range(3)):
            return True
    return False

# Function to count gold slots
def count_gold():
    gold_count = 0
    for x, y in gold_positions:
        rgb = get_rgb_at_position(x, y)
        if rgb != no_gold_ref and is_gold_color(rgb):
            gold_count += 1
    return gold_count

# Main execution in a while loop to check every 2 seconds
if __name__ == "__main__":
    try:
        while True:
            gold_amount = count_gold()
            print(f"Your current gold amount is: {gold_amount} gold.")
            time.sleep(2)  # Wait for 2 seconds before checking again
    except KeyboardInterrupt:
        print("Program stopped.")




