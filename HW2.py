# HW2.py
# Author: Anna-Marie DiNofrio


# Question 1:
# Write some code that prompts the user for their age. Depending on the input:

# If the age is less than 13, print "You are a child."
# If the age is between 13 and 19, print "You are a teenager."
# If the age is 20 or older, print "You are an adult."

age = int(input("What is your age? "))
if age < 13:
    print("You are a child.")
elif 13 <= age <= 19:
    print("You are a teenager.")
elif age >= 20:
    print("You are an adult.")

    
# Question 2:
# Write some code to display the following pattern using a for or while loop:
# 1
# 12
# 123
# 1234
# 12345

i = 1
pattern = str(i)
while i <= 5:
    print(pattern)
    i += 1  #i = i + 1
    pattern += str(i)
    
# Question 3:
# Write some code that prompts the user to input 10 numbers. After all the numbers are inputted, the program should display:

# The highest number.
# The lowest number.
# The average of all the numbers.

# Hint 1: You will need to use a for loop and a counter variable to keep track of the total sum of the numbers.
# Hint 2: You will need to use an if statement to keep track of the highest and lowest numbers.
# print("Please enter ten random numbers.")
i = 1
sum = 0
numbers = int(input("Enter numbers. "))
highest_number = numbers
lowest_number = numbers
while i < 10:
    numbers = int(input("Enter numbers. "))
    i += 1
    sum += numbers
    if numbers > highest_number:
        highest_number = numbers
    if numbers < lowest_number:
        lowest_number = numbers
average = sum/10
print("The average is " + str(average)) 
print("The highest number is " + str(highest_number))
print("The lowest number is " + str(lowest_number))


# Question 4:
# Vowel Counter - Write some code that prompts the user to enter a string. The program should then display the number of vowels in the string. IE. If the user enters "Hello World", the program should display 3.
# the vowels are a, e, i, o, u
# Hint: convert the string to lowercase and use a for loop with a counter variable and an if statement

string = input("Enter a word. ")
string = string.lower()
vowels = 0
for i in string:
    if i in "aeiou":
        vowels += 1
print("The numbers of the vowels in the word is " + str(vowels))
       
    