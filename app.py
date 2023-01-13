import math

def calculator(num1,num2):

    operation = input("enter the operation you want to perform : +, -, /, *, %, **, sqrt: ")

    if operation == "+":
        print(num1 + num2)
    elif operation == "-":
        print(num1-num2)
    elif operation == "/":
        print(num1/num2)
    elif operation == "*":
        print(num1*num2)
    elif operation == "**":
        print(num1**num2)
    elif operation=="sqrt":
        print(match.sqrt(num1))
    else :  
        print("please enter a valid value from the one proposed.")

def get_valid_input(prompt):
    while True:
        user_input = input(prompt)
        if user_input.isdigit():
            return float(user_input)
        else:
            print("invalide input, please enter a numeric value")        

while True:

    num1 = get_valid_input("enter the first number : ")
    num2 = get_valid_input("enter the second number : ")


    calculator(num1,num2)
    exit_choice = input("to exit type q otherwise type Enter or any other key to Continue: ")
    if exit_choice == "q":
        break

