import random


destionations = [" england" , "sweden", "denmark"]

def wheretowhere ():
    doublechecker = []
    doublechecker.append(random.choices(destionations))

    while len(doublechecker) >2:
            if random.choice(destionations) not in doublechecker:
                doublechecker.append(random.choices(destionations))



    print(f"Today you are flying from {random.choice(destionations)} to {random.choice(destionations)}")


## i want to make  sure they cant be doubles

wheretowhere()