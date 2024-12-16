'''
PRACTICE: MCQUIZ

Write a Python program to play a multiple-choice quiz.

1. Set up a list of multiple-choice questions with 2, 3 or 4 possible answers.
1. You will also need some way of storing the correct answer.
2. From this list randomly select a question and its choices.
3. Display the question and choices and ask the user for their answer.
4. Check the user’s answer, keeping score of correct and incorrect answers.
5. After 10 questions,

'''

import random

###1. Set up a list of multiple-choice questions with 2, 3 or 4 possible answers.

qone = ["How do you read a CSV file into a Pandas DataFrame?" ,
       "a) Using the load_csv function",
       "b) Using the read_csv function",
       "c) Using the open_file function"
        ,"d) Using the import_data function"]

qtwo = ["What method is used to drop rows containing NaN values in a Pandas DataFrame, and why is it important?", 
        "a) remove_null - It helps in cleaning the data" ,
        "b) dropna - It helps in handling missing data",
        "c) clean_data - It helps in reshaping the DataFrame",
        " d) filter_null - It helps in sorting the data"]

qthree = [ "What is correlation, and how is it used to analyze relationships between variables in a dataset?" ,
           "a) It measures the strength and direction of a linear relationship between two variables",
           " b) It calculates the mean of the dataset ",
             "c) It identifies outliers in the data ", 
             "d) It performs clustering of data points" ]

qfour = [ "Describe the process of calculating the mean, standard deviation, and variance of a dataset using NumPy." ," a) Using the mean, std, and var functions ","b) Using the calculate_mean, calculate_std, and calculate_var functions"," c) Using the average, deviation, and variance functions", "d) Using the compute_mean, compute_std, and compute_var functions"  ]


qfive = ["What is the purpose of creating a scatter plot in data analysis, and how does it help in visualizing relationships between variables? ", "a) To visualize the spread of the data"," b) To visualize the distribution of the data"," c) To visualize the relationship between two variables", " d) To visualize the trend of the data "]

questionlist = [qone, qtwo, qthree, qfour, qfive]
# correctans = [q1 = b , q2 = b, q3 = a, q4 = a , q5 = c ]



def questionprompt():

    qa = 0
    correctscore = 0
    wrongscore = 0 
    while qa < 6:

        randomselect = random.sample(questionlist, k=1)

        print("-" * 60)
        for question in randomselect:
            for line in question:
                print(line)

        
        if randomselect[0] == qone:
            correct = "b"
        elif randomselect[0] == qtwo:
            correct = "b"
        elif randomselect[0] == qthree:
            correct = "a"
        elif randomselect[0] == qfour:
            correct = "a"
        elif randomselect[0] == qfive:
            correct = "c"
       
        #print(correct)
        answer = input("Type the letter to answer : ")   ### check for abcd
        
        if answer == correct:
            correctscore += 1
            qa += 1 
            print("-" * 60)
            print("Correct!!")
            print("-" * 60)
        else:
            wrongscore += 1
            qa += 1 
            print("-" * 60)
            print("incorrect")
            print("-" * 60)

    print(f"You got {correctscore} right and {wrongscore} wrong")

############ Main processing

questionprompt()





