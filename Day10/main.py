from art import logo
import subprocess
import os

def clear():
    subprocess.run('cls' if os.name == 'nt' else 'clear')

operations = {
    "+": lambda a, b: a + b,
    "-": lambda a, b: a - b,
    "*": lambda a, b: a * b,
    "/": lambda a, b: a / b,
}

def first_operation():
    dict_values = {}
    number1 = int(input("What's the first number?: "))
    print("+\n-\n*\n/")
    operator = input("Pick an operation: ")
    number2 = int(input("What's the second number?: "))
    result = operations[operator](number1, number2)
    dict_values["number1"] = number1
    dict_values["operator"] = operator
    dict_values["number2"] = number2
    dict_values["result"] = result
    return dict_values

def calculator():
    run = True
    values = list(first_operation().values())
    print(f'Result: {values[0]} {values[1]} {values[2]} = {values[3]}')
    while run:
        result = values[3]
        option = input(f'Type y to continue calculating with {result}, or type n to start a new calculation:')
        if option == "y":
            print("+\n-\n*\n/")
            operator = input("Pick an operation: ")
            next_number = int(input("What's the next number?: "))
            next_operations = operations[operator](result, next_number)
            print(f'Result: {result} {operator} {next_number} = {next_operations}')
            values[3] = next_operations
        else:
            run = False
            clear()

calculator()