
'''
# Goal of the program is to win decently at pvp in warcraft rumble


# the cost of the minions are shown in the number attached to the end of the pngs.




# Playbook logic

# Best play is to play the emp minion, followed by the ranger or troll, this is only possible if we can detect that emp, + troll or ranger is in our hand,


otherwise we play the lowest cost minion in hand, to try to cycle back around to troll and ranger, we want to play them as often as possible


we only try to play them if we have the gold required to do so

to play a minion we to select it by pressing 1 for slot 1 2 for slot 2 etc 
then we click somewhere on the screen, for now i want to limit the area to a region of randomness around 3 points below + or - 20 pixel locations to avoid detection

#     (1475, 945),
#     (1265, 778),
#     (1037, 940)







# g
# ###Team checker function

# ## region of team icons = Region: (1045, 1203, 628, 140)

# ## region of icons
# # slot one = Region: (1049, 1197, 151, 120) 
# # slot two  =  Region: (1205, 1197, 127, 114)
# # slot three = Region: (1356, 1201, 148, 106)
# # slot four =  Region: (1511, 1201, 134, 111)




}


# minion_info = {
#     "Bandit": {"cost": 1, "image": "greyscale_Bandit 1.png"},
#     "DI miner": {"cost": 2, "image": "greyscale_DI miner 2.png"},
#     "Emp": {"cost": 4, "image": "greyscale_Emp 4.png"},
#     "Gryf": {"cost": 2, "image": "greyscale_Gryf 2.png"},
#     "Pyro": {"cost": 3, "image": "greyscale_Pyro 3.png"},
#     "Ranger": {"cost": 5, "image": "greyscale_Ranger 5.png"},
#     "Rat miner": {"cost": 1, "image": "greyscale_Rat miner 1.png"},
#     "Troll": {"cost": 3, "image": "greyscale_Troll 3.png"}

# }
'''
##################################################################################################


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

# Main function to continuously check gold every 2 seconds
def check_gold_continuously():
    try:
        while True:
            gold_amount = count_gold()
            print(f"Your current gold amount is: {gold_amount} gold.")
            time.sleep(2)  # Wait for 2 seconds before checking again
    except KeyboardInterrupt:
        print("Program stopped.")

# To use the function in your broader program, you can call:
# check_gold_continuously()

##################################################################################################
# import pyautogui
# import time

# # Reference RGB values for gold slots (within a reasonable tolerance range)
# gold_refs = [
#     (209, 186, 55), (208, 188, 65), (209, 190, 66), (239, 226, 84), 
#     (251, 224, 82), (255, 232, 82), (254, 222, 75), (255, 233, 79), 
#     (250, 225, 80), (255, 230, 74)
# ]

# # Reference RGB value for "no gold"
# no_gold_ref = (27, 27, 27)

# # Positions of the gold slots
# gold_positions = [
#     (1129, 1402), (1188, 1396), (1253, 1395), (1301, 1400), 
#     (1350, 1399), (1404, 1399), (1469, 1398), (1519, 1395), 
#     (1577, 1395), (1630, 1401)
# ]

# # Function to get RGB value from a position
# def get_rgb_at_position(x, y):
#     return pyautogui.screenshot(region=(x, y, 1, 1)).getpixel((0, 0))

# # Function to determine if a color is close to the reference color
# def is_gold_color(rgb, tolerance=30):
#     for ref in gold_refs:
#         if all(abs(rgb[i] - ref[i]) <= tolerance for i in range(3)):
#             return True
#     return False

# # Function to count gold slots
# def count_gold():
#     gold_count = 0
#     for x, y in gold_positions:
#         rgb = get_rgb_at_position(x, y)
#         if rgb != no_gold_ref and is_gold_color(rgb):
#             gold_count += 1
#     return gold_count

# # Main execution in a while loop to check every 2 seconds
# if __name__ == "__main__":
#     try:
#         while True:
#             gold_amount = count_gold()
#             print(f"Your current gold amount is: {gold_amount} gold.")
#             time.sleep(2)  # Wait for 2 seconds before checking again
#     except KeyboardInterrupt:
#         print("Program stopped.")
# ##################################################################################################




# #Secondly is gold getting with dark iron miner
# gotta screenshot the screen to look for gold nodes

# if  gold count > 6 and gold node found, with > 1 gold, and DI miner in hand, pick DI and place and region that node is found



# finally if the screenshot of our base regoin at the begining is different from the starting version. place a minion a 100 pixel south of the region where change is detected ( attempt to defend from minon)






# screencap at the start of a match, this is to compare the empty space around the base, so when an enemy enters i.e change detected, we can place a minion to defend below that difference region

