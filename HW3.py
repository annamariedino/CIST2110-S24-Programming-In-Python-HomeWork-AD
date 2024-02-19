# HW3.py
# Author: Anna-Marie DiNofrio

# This Homework assignment is meant to test your ability to make functions within python as well as importing and using modules. This assignment might require you to do some research on your own. If you get stuck, try googling the problem, especially when it comes to importing and using the different modules.

# Hint you will want to enable word wrap in vscode (View -> Toggle Word Wrap) to make it easier to read the instructions.

# Question 1:
# Write a function that takes in a number and returns that number squared
# IE. If the user inputs 3, the function should return 9
def squared(x):
    """This function takes in a number and returns that number squared
    Args:
        x (int): The number to be squared"""
    return x**2
print(squared(3))

# Question 2:
# Write a function that takes in a string, a letter, and a number and returns the string with the letter replaced at the number index
# IE. If the user inputs "Hello World", "a", and 3, the function should return "Helao World"
# Hint: You will want to use the replace() function
def replace_letter (string, letter, number):
    """This function taked in a string, a letter, and a number and returns the string with the letter replaced at the number index
    Args:
        string (str): The string to be modified
        letter (str): The letter to be replaced
        number (int): The index of the letter to be replaced"""
    return string[:number] + letter + string[number+1:]
print(replace_letter("Hello World", "a", 3))

# Question 3:
# Write a function that takes in a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
# IE. If the user inputs 5, 1, and 10, the function should return True
def within_bounds (number, lower_bound, upper_bound):
    """This function takes a number, a lower_bound, and an upper_bound and returns whether the number is within the bounds
    Args:
        number (int): The number to be checked
        lower_bound (int): The lower bound
        upper_bound (int): The upper bound"""
    return lower_bound <= number <= upper_bound
print(within_bounds(5, 1, 10))

# Question 4:
# write a function with parameters for a name, age, and favorite color. Return the following string using the parameters:
# "Hello, my name is <name>. I am <age> years old. My favorite color is <color>."
def personal_info (name, age, color):
    """This function takes in a name, age, and favorite color and returns a string with the parameters
    Args:
        name (str): The name of the person
        age (int): The age of the person
        color (str): The favorite color of the person"""
    return f"Hello, my name is {name}. I am {age} years old. My favorite color is {color}."
print(personal_info("Max", 21, "blue"))
    
# Question 5:
# Write a function that asks the user for their name, age, and favorite color and then calls the function from question 4 using the user's input as the parameters.
# Hint: You will want to save the users input to variables and use them as the parameters for the function from question 4
def user_info ():
    """This function asks the user for their name, age, and favorite color and then calls the function from Q4 using the user's previous input as the parameters"""
    name = input("What is your name? ")
    age = input("How old are you? ")
    color = input("What is your favorite color? ")
    return personal_info(name, age, color)
print(user_info())
    
# Question 6:
# import the random module and use it to generate a random number between 1 and 100
def random_number ():
    """This function generates a random number between 1 and 100"""
    import random
    return random.randint(1, 100)
print(random_number())

# Question 7: (research)
# import the math module and use it to find the square root of 16 (hint: use the sqrt() function)
def square_root ():
    """This function uses the math module to find the square root of 16"""
    import math
    return math.sqrt(16)
print(square_root())

# Question 8:
# import the sys module and use it to print the version of python you are using
# this time import the module using the import "as" keyword
# hint: use the version attribute (sys.version)
def python_version ():
    """This function uses the sys module to print the version of python being used
    Args:
        version (str): The version of python being used"""
    import sys as s
    return s.version
print(python_version())

# Question 9: (research)
# import the os module and use it to print the current working directory. This time import the module using the from keyword
# hint: use the getcwd() function
def current_directory ():
    """This function uses the os module to print the current working directory
    Args:
        directory (str): The current working directory"""
    from os import getcwd
    return getcwd()
print("here!!" + current_directory())
