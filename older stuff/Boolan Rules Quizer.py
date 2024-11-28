import random

# Dictionary of Boolean laws with examples and descriptions
boolean_laws = {
    "Identity Law": [
        ("A AND 1", "A"),
        ("A OR 0", "A")
    ],
    "Null Law": [
        ("A AND 0", "0"),
        ("A OR 1", "1")
    ],
    "Complement Law": [
        ("A AND NOT A", "0"),
        ("A OR NOT A", "1")
    ],
    "Idempotent Law": [
        ("A AND A", "A"),
        ("A OR A", "A")
    ],
    "Domination Law": [
        ("A AND 0", "0"),
        ("A OR 1", "1")
    ],
    "Double Negation Law": [
        ("NOT (NOT A)", "A")
    ]
}

# Function to generate the truth table for a Boolean expression
def generate_truth_table(expression, law):
    print("\nTruth Table:")
    print(f"Law: {law}")
    print("A | Result")
    print("---------")
    # Generate truth values for A (0 and 1)
    for A in [0, 1]:
        # Evaluate the expression
        if expression == "A AND 1":
            result = A and 1
        elif expression == "A OR 0":
            result = A or 0
        elif expression == "A AND 0":
            result = A and 0
        elif expression == "A OR 1":
            result = A or 1
        elif expression == "A AND NOT A":
            result = A and not A
        elif expression == "A OR NOT A":
            result = A or not A
        elif expression == "NOT (NOT A)":
            result = not (not A)
        else:
            result = None

        print(f"{A} | {result}")

# Function to quiz the user
def quiz_user():
    score = 0
    total_questions = 0
    law_keys = list(boolean_laws.keys())
    random.shuffle(law_keys)  # Randomize the order of laws
    used_laws = []

    while True:
        if not law_keys:  # Reset when all laws have been used
            law_keys = used_laws[:]
            random.shuffle(law_keys)
            used_laws = []

        law = law_keys.pop()  # Select the next law
        used_laws.append(law)
        expression, correct_answer = random.choice(boolean_laws[law])
        total_questions += 1

        # Suggest the law to solve the expression
        print(f"\n----- New Question -----")
        print(f"Using {law}, simplify the following expression: {expression}")
        
        while True:
            user_answer = input("Your answer (type 'hint' or 'h' for a hint): ").strip().lower()
            
            if user_answer == "exit":
                print(f"\nYour final score is: {score}/{total_questions}")
                return
            
            if user_answer in ["hint", "h"]:
                # Display the description of the law used
                if law == "Identity Law":
                    print("\nThe Identity Law shows that when you combine a value with 1 using AND, or combine a value with 0 using OR, the original value is unchanged. "
                          "This happens because AND with 1 keeps the original value, and OR with 0 does not affect it.")
                elif law == "Null Law":
                    print("\nThe Null Law shows that the result of ANDing a value with 0 is always 0 because 0 'nullifies' the other value, while ORing a value with 1 always results in 1 "
                          "because 1 dominates the OR operation, making the result true regardless.")
                elif law == "Complement Law":
                    print("\nThe Complement Law shows that a value and its complement (NOT) can never both be true. "
                          "The AND of a value and its complement is always false, while the OR of a value and its complement is always true, because one must be true.")
                elif law == "Idempotent Law":
                    print("\nThe Idempotent Law shows that performing the same operation twice on the same value does not change the outcome. "
                          "Whether ANDing or ORing a value with itself, the result is always the same value.")
                elif law == "Domination Law":
                    print("\nThe Domination Law illustrates that 0 in AND or 1 in OR will 'dominate' the outcome. "
                          "ANDing with 0 always results in 0, and ORing with 1 always results in 1, regardless of the other value.")
                elif law == "Double Negation Law":
                    print("\nThe Double Negation Law tells us that negating a value twice brings it back to the original value. "
                          "The first negation flips the value, and the second negation flips it back.")
                continue  # Re-prompt for the answer after showing the hint
            
            # Check if the user's answer is correct
            if user_answer == correct_answer.lower():
                print("Correct!\n")
                score += 1
                break  # Correct answer, move to the next question
            else:
                # Show the description of the law for incorrect answers
                if law == "Identity Law":
                    print("\nThe Identity Law shows that when you combine a value with 1 using AND, or combine a value with 0 using OR, the original value is unchanged. "
                          "This happens because AND with 1 keeps the original value, and OR with 0 does not affect it.")
                elif law == "Null Law":
                    print("\nThe Null Law shows that the result of ANDing a value with 0 is always 0 because 0 'nullifies' the other value, while ORing a value with 1 always results in 1 "
                          "because 1 dominates the OR operation, making the result true regardless.")
                elif law == "Complement Law":
                    print("\nThe Complement Law shows that a value and its complement (NOT) can never both be true. "
                          "The AND of a value and its complement is always false, while the OR of a value and its complement is always true, because one must be true.")
                elif law == "Idempotent Law":
                    print("\nThe Idempotent Law shows that performing the same operation twice on the same value does not change the outcome. "
                          "Whether ANDing or ORing a value with itself, the result is always the same value.")
                elif law == "Domination Law":
                    print("\nThe Domination Law illustrates that 0 in AND or 1 in OR will 'dominate' the outcome. "
                          "ANDing with 0 always results in 0, and ORing with 1 always results in 1, regardless of the other value.")
                elif law == "Double Negation Law":
                    print("\nThe Double Negation Law tells us that negating a value twice brings it back to the original value. "
                          "The first negation flips the value, and the second negation flips it back.")

                print(f"Incorrect! The correct answer is {correct_answer}\n")
                break  # Incorrect answer, move to the next question
        
        # Display the truth table for the expression after the answer
        generate_truth_table(expression, law)

# Run the quiz
quiz_user()
