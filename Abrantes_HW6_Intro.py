""" Nathan Abrantes 
    23 February 2025
    Homework #6   
"""

#A couple of questions that asks for two numbers that are executed in different mathematical ways.
answer = input("Hello Professor! Please provide me with two numbers and I will output them in various mathematical ways! Please give me the first number! ")
print(f"You answered: {answer}!")
print("\n")

answer1 = input("Give me the second number! ")
print(f"You answered: {answer1}!")
print("\n")

#Arithmetic Operations:
addition = int(answer) + int(answer1)
multiply = int(answer) * int(answer1)
divide = int(answer) / int(answer1)
subtract = int(answer) - int(answer1)

#Answers:
print(f"Addition: {addition}")
print(f"Multiplication: {multiply}")
print(f"Division: {divide}")
print(f"Subtraction: {subtract}")
print("\n")

print("Thank you Professor! Come again!")