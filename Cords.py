 
import random
 
questions = {
 
    "Q1": {"qText": "What is the capital of England",          
           "qChoices": {
 
                "choice1": "London",
                "choice2": "Bromley",
                "choice3": "Glasgow",
                "choice4": "Hackney",
                "correct": "London" }
            },
 
    "Q2": {"qText": "What is the Capital of France",          
            "qChoices": {
               "choice1": "Croydon",
               "choice2": "Normandy",
               "choice3": "Paris",
                "choice4": "Leon",
                "correct":"Paris" },
    },
 
    "Q3": {"qText": "What is the Capital of Spain",          
            "qChoices": {
                "choice1": "xxxx",
                "choice2": "yyyyy",
                "choice3": "zzzz",
                "choice4": "aaaa",
                "correct":"zzzz" }
    }
 
    }

thisQuestion = ( random.choice(list(questions.keys())))
 
print(type(thisQuestion))
print(questions[thisQuestion]["qText"])

# k = bookDict.keys()
# print(k)
 
 
qchoiceskeys = list(questions[thisQuestion]["qChoices"].keys())
print(qchoiceskeys)
 
qchoiceskeys.pop()
# for choice in questions[thisQuestion]["qChoices"]:
#    print(questions[thisQuestion]["qChoices"])
 
 