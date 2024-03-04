# Project1.py
# Author: Anna-Marie DiNofrio


# This project is meant to test your ability from everything we have learned so far in class
# You will need to use variables, if statements, loops, and functions

# Quiz Game:
# Create a simple console-based quiz game where the user answers a series of questions.
# The game should keep track of the user's score and provide feedback based on the answers given.

# Global Vars
score = 0
# Write a function that displays a welcome message to the user and explains the rules of the game
welcome_message = input("Welcome to the quiz game! You will be asked a series of 5 questions and will be given 4 options to choose from. Please choose the letter of the answer you think is correct. You will be given a score at the end of the game. Press enter to continue.")
# Implement at least 5 questions, each with 4 answer options (a, b, c, d). Each question should be worth 1 point.
# For each question, display the question and the answer options to the user.
# Use input() to get the user's answer.
# Use if or if-else statements to check if the answer is correct.
# If the answer is correct, display a positive feedback message and add points to the user's score.
# If the answer is incorrect, display a negative feedback message and provide the correct answer.
# Score Tracking:
# Question_1 = input("How many toes does a parrot have?\nA) Three\nB) Five\nC) Four\nD) Six\n")
# if Question_1.lower == "C":
#     print("Correct!")
# else: 
#     print("Incorrect. The correct answer is C) Four")

# Question_2 = input("What do bees collect from flowers?\nA) Pollen\nB) Nectar\nC) Water\nD) Both Pollen and Nectar\n")
# if Question_2.lower == "D":
#     print("Correct!")
# else:   
#     print("Incorrect. The correct answer is D) Both Pollen and Nectar")

# Question_3 = input("How long does it take to germiinate bell pepper seeds?\nA) 3-5 days\nB) 3 weeks\nC) 1 month\nD) 1-2 weeks\n")
# if Question_3.lower == "D":
#     print("Correct!")
# else:   
#     print("Incorrect. The correct answer is D) 1-2 weeks")

# Question_4 = input("What is the most popular fruit in the world?\nA) Apple\nB) Banana\nC) Orange\nD) Mango\n")
# if Question_4.lower == "B":
#     print("Correct!")
# else:
#     print("Incorrect. The correct answer is B) Banana")

# Question_5 = input("What are ocean waves most commonly caused by?\nA) The moon\nB) Wind\nC) Sand Bars\nD) Boats\n")
# if Question_5.lower == "B":
#     print("Correct!")
# else:
#     print("Incorrect. The correct answer is B) Wind")


## Start of ask question function


def ask_question (question:str, option_1:str, option_2:str, option_3:str, option_4:str, correct_answer:str) -> bool:
    """This function asks a question and checks the answer. This function should accept parameters like the question, options, the correct answer, and return whether the user was correct.
    Args:
        question (str): The question to be asked
        option_1 (str): The first option for the user to choose from
        option_2 (str): The second option for the user to choose from
        option_3 (str): The third option for the user to choose from
        option_4 (str): The fourth option for the user to choose from
        correct_answer (str): The correct answer to the question
        
    Returns:
        Bool: If the user got the answer correct    
    """
    # Print the Question and Options
    print(question)
    print("A:",option_1)
    print("B:",option_2)
    print("C:",option_3)
    print("D:",option_4)
    # Ask user for input
    user_answer = input ("Please enter the correct answer: A B C or D\n")
    # Check if user_input matches correct_answer STR == STR
   
    if user_answer.lower() == correct_answer:
        return True
    
    

    while user_answer.lower() != "a" or "b" or "c" or "d":
        print("Please enter a valid answer: A B C or D\n")
        user_answer = input ("Please enter the correct answer: A B C or D\n")
        if user_answer.lower() == correct_answer:
            return True
        else: 
            continue
          
        
Question_1 = ask_question("How many toes does a parrot have?","Three","Five","Four","Six","c")
print(Question_1)

Question_2 = ask_question("What do bees collect from flowers?","Pollen","Nectar","Water","Both Pollen and Nectar","d")
print(Question_2)

Question_3 = ask_question("How long does it take to germinate bell pepper seeds?","3-5 days","3 weeks","1 month","1-2 weeks","d")
print(Question_3)

Question_4 = ask_question("What is the most popular fruit in the world?","Apple","Banana","Orange","Mango","b")
print(Question_4)

Question_5 = ask_question("What are ocean waves most commonly caused by?","The moon","Wind","Sand Bars","Boats","b")
print(Question_5)

# Define function
def calc_score(question):
    global score  # Declare 'score' as a global variable
    if question == True:
        score += 1

# Calling the function (more defined with vars)
calc_score(Question_1)
calc_score(Question_2)
calc_score(Question_3)
calc_score(Question_4)
calc_score(Question_5)

print(f"Your score is {score} out of 5. Thanks for playing!")


# def calculate_score(score):
    # Print a nice message with the score (String concat)


# Keep track of the user's score throughout the game.
# After all questions have been answered, display the user's total score and a farewell message.
# Function Utilization:


# print(f"Your score is {score} out of 5. Thanks for playing!")


# Create a function to ask a question and check the answer. This function should accept parameters like the question, options, the correct answer, and return whether the user was correct.
# an example would be def ask_question(question:str, option_1:str, option_2:str, option_3,:str option_4:str, correct_answer:str)->bool:
# the return value should be a boolean (True or False) for whether the user was correct



# Create a function to display the final score, which takes the score as a parameter and displays a message.
# Loops:
# Use a for or while loop to iterate through the questions.
# Variable Casting:
# Ensure that user input is cast and checked appropriately to avoid errors during execution.
# Error Handling:
# Implement basic error handling to manage invalid inputs from the user (e.g., an answer other than a, b, c, or d).

