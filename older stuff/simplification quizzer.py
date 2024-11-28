import random

# List of Boolean simplification problems with expected results and hints
problems = [
    {"expression": "A AND 1", "answer": "A", "law": "Identity Law"},
    {"expression": "A OR 0", "answer": "A", "law": "Identity Law"},
    {"expression": "A AND 0", "answer": "0", "law": "Null Law"},
    {"expression": "A OR 1", "answer": "1", "law": "Null Law"},
    {"expression": "A AND NOT A", "answer": "0", "law": "Complement Law"},
    {"expression": "A OR NOT A", "answer": "1", "law": "Complement Law"},
    {"expression": "A AND A", "answer": "A", "law": "Idempotent Law"},
    {"expression": "A OR A", "answer": "A", "law": "Idempotent Law"},
    {"expression": "NOT (NOT A)", "answer": "A", "law": "Double Negation Law"},
    {"expression": "(A OR 0) AND A", "answer": "A", "law": "Identity and Idempotent Laws"},
    {"expression": "(A AND 1) OR 1", "answer": "1", "law": "Identity and Domination Laws"},
    {"expression": "A AND (A OR B)", "answer": "A", "law": "Absorption Law"},
    {"expression": "A OR (A AND B)", "answer": "A", "law": "Absorption Law"},
    {"expression": "NOT (A AND B)", "answer": "NOT A OR NOT B", "law": "De Morgan's Laws"},
    {"expression": "NOT (A OR B)", "answer": "NOT A AND NOT B", "law": "De Morgan's Laws"},
    {"expression": "(A OR B) AND A", "answer": "A", "law": "Absorption Law"},
    {"expression": "(A AND B) OR A", "answer": "A", "law": "Absorption Law"},
    {"expression": "A AND (NOT A OR B)", "answer": "A AND B", "law": "Distributive Law"},
    {"expression": "A OR (A AND NOT B)", "answer": "A", "law": "Distributive Law"},
    {"expression": "(A OR B) AND (A OR NOT B)", "answer": "A", "law": "Consensus Theorem"}
]

import re  # Import the regex module

def generate_truth_table(expression, simplified, law):
    print("\nTruth Table:")
    print(f"Law: {law}")
    print("A | B | Original | Simplified")
    print("-----------------------------")
    for A in [0, 1]:
        for B in [0, 1]:
            # Use regex to safely replace logical operators
            expr_eval = re.sub(r"\bAND\b", "and", expression)
            expr_eval = re.sub(r"\bOR\b", "or", expr_eval)
            expr_eval = re.sub(r"\bNOT\b", "not", expr_eval)
            simp_eval = re.sub(r"\bAND\b", "and", simplified)
            simp_eval = re.sub(r"\bOR\b", "or", simp_eval)
            simp_eval = re.sub(r"\bNOT\b", "not", simp_eval)

            # Evaluate expressions
            original_result = eval(expr_eval.replace("A", str(A)).replace("B", str(B)))
            simplified_result = eval(simp_eval.replace("A", str(A)).replace("B", str(B)))

            # Print the truth table row
            print(f"{A} | {B} |    {int(original_result)}     |     {int(simplified_result)}")


# Function to provide a hint based on the law
def show_hint(law):
    if law == "Identity Law":
        return "Combining with 1 using AND or 0 using OR does not change the value."
    elif law == "Null Law":
        return "ANDing with 0 always results in 0, and ORing with 1 always results in 1."
    elif law == "Complement Law":
        return "A value ANDed with its complement is always 0; ORed with its complement is always 1."
    elif law == "Idempotent Law":
        return "Repeating the same operation (AND/OR) on a value doesn't change it."
    elif law == "Double Negation Law":
        return "Negating twice returns the original value."
    elif law == "Absorption Law":
        return "A dominates when combined with (A OR B) using AND, or (A AND B) using OR."
    elif law == "De Morgan's Laws":
        return "NOT (A AND B) = NOT A OR NOT B; NOT (A OR B) = NOT A AND NOT B."
    elif law == "Distributive Law":
        return "Distribute AND/OR over a grouped expression (similar to algebra)."
    elif law == "Consensus Theorem":
        return "Redundant terms can be eliminated when covered by another part of the expression."
    else:
        return "No hint available."

# Function to quiz the user
def quiz_user():
    score = 0
    total_questions = 0
    used_problems = []
    remaining_problems = problems[:]
    random.shuffle(remaining_problems)

    while True:
        if not remaining_problems:  # Reset when all problems have been used
            remaining_problems = used_problems[:]
            used_problems = []
            random.shuffle(remaining_problems)

        problem = remaining_problems.pop()  # Select the next problem
        used_problems.append(problem)
        expression = problem["expression"]
        correct_answer = problem["answer"]
        law = problem["law"]
        total_questions += 1

        print(f"\n----- New Question -----")
        print(f"Simplify the following expression: {expression} (Hint: {law})")

        while True:
            user_answer = input("Your answer (type 'h' for a hint): ").strip().lower()
            
            if user_answer == "exit":
                print(f"\nYour final score is: {score}/{total_questions}")
                return
            
            if user_answer in ["hint", "h"]:
                print(f"\nHint: {show_hint(law)}")
                continue  # Re-prompt for the answer after showing the hint
            
            if user_answer == correct_answer.lower():
                print("Correct!\n")
                score += 1
                break  # Move to the next question
            else:
                print(f"Incorrect! The correct answer is {correct_answer}\n")
                print(f"Hint: {show_hint(law)}")
                break  # Move to the next question

        # Display the truth table for the expression after the answer
        generate_truth_table(expression, correct_answer, law)

# Run the quiz
quiz_user()
