# Program to show processing lists within lists
 
grades = [   ["Mark  ", 23,45,43,67,78],

             ["Jenny ", 34,65,78,56,34],

             ["Fatima", 34,65,78,56,45],

             ["Rupert", 45,65,45,67,34 ],

             ["Mags  ", 45,65,45,67,34 ],

             ["Rupp  ", 45,65,45,67,34 ],

             ["Mary  ", 45,65,45,67,34 ],

             ["Rupert", 45,65,45,67,34 ],

             ["Maggie", 45,65,45,67,34 ]
 
          ]

list = ["Maggie", 45,65,45,67,34 ]


        

 
def printScores():
 
    print("Length", len(grades))
 
    print(f"Name \t\t Total \t Average")

    print(f"---- \t\t ----- \t -------")

    # outer FOR loop for all students

    for i in range(0, len(grades) ):

        total = 0   # reset total score

        # inner FOR loop for one student's scores

        for j in range(1, len(grades[i]) ):

            total = total + grades[i][j]      # accumulate the total

        print(f" {grades[i][0]} \t {total} \t {total /(len(grades[i])-1)} ")   

 
 
#----- MAIN PROCESSING ---------

printScores()       # print the scores
 
 
 