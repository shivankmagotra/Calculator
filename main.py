from os import system, name
# import sleep to show output for some time period
from time import sleep
# define our clear function
def clear():
    # for windows
    if name == 'nt':
        _ = system('cls')
    # for mac and linux(here, os.name is 'posix')
    else:
        _ = system('clear')
from art import logo
#Add function
def add(n1, n2):
  return n1 + n2
#Subtract function
def subtract(n1, n2):
  return n1 - n2
#Multiply function
def multiply(n1, n2):
  return n1 * n2
#Divide function
def divide(n1, n2):
  return n1 / n2
#Operators dictionary
operations = {
  "+": add,
  "-": subtract,
  "*": multiply,
  "/": divide
}
#Calculate function
def calculator():
  print(logo)

  num1 = float(input("What's the first number?: "))
  for symbol in operations:
    print(symbol)
  should_continue = True
 
  while should_continue:
    operation_symbol = input("Pick an operation: ")
    num2 = float(input("What's the next number?: "))
    calculation_function = operations[operation_symbol]
    answer = calculation_function(num1, num2)
    print(f"{num1} {operation_symbol} {num2} = {answer}")

    if input(f"Type 'y' to continue calculating with {answer}, or type 'n' to start a new calculation: ") == 'y':
      num1 = answer
    else:
      should_continue = False
      clear()
      calculator()
#Main program
calculator()