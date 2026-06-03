#----------Functions and arguments----------

def greet():
    print("hello!!!!")
greet()

#-------with parameters--------------

def greet(name):
    print(f"hello {name}")
greet('sameer')


def add(a,b):
    return a+b

result = add(6,7)
print(result)


def min_max(numbers):
    return min(numbers), max(numbers)
low,high = min_max([1,2,3,5,43,22,21])
print(low,high)

#----default arguments----------#

def greet(name, greeting = 'hello'):
    print(f"{greeting}!!, {name}")
greet('sameer') #default will be automatically printed
greet('Sameer','Salam')  # default value can be overwritten

#-------function with keyword--------#

def create_profile(name,city,age):
    print(f"{name} | {city} | {age}")

create_profile(name='sameer', age = 20, city = 'Gujrat')  #order doesn't matter if we use keyword as parameter

#-----global and local scope variable---#
 
description = "Global and local variable scope is same as u have studied in c++"

#----args , kwargs-------------#

#args* is used as a parameter in the function where we dont know the exact no. of parameters that can be applied here so we put *args as a parameter that takes all arguments for the function
def add(*args):
    print(args)
    return sum(args)
print(add(1,2,3,4,5))
print(add(10,20))
# *args gives us the parameters or arguments in the form of tuples

#**kwargs gives us the data in the form of dictionary
def create_profile(**kwargs):
    print(kwargs)
    for key, value in kwargs.items():
        print(f"{key}: {value}")

create_profile(name='sameer', age = 20, city = 'Gujrat')

create_profile(name = 'Ali', age = 20, city = 'Lahore', country = 'Pakistan')

#combining everything

def everything(required, *args,**kwargs):
    print(f"Required: {required}")
    print(f"Args: {args}")
    print(f"kwargs: {kwargs}")

everything('Hello',1,2,3,4,name = 'sameer', age = 22)


#-----Lambda functions---------#
desc= "Lambda is a special type of function which is actually shorter format of the normal function . It is particularly used for sort , map and filter functions where shorter form of functions are required."

add = lambda a,b : a+b
print(add(5,7))

numbers = [3,5,1,4,7,8,3,9]
sorted_numbers = sorted(numbers, key=lambda x: x)
print(sorted_numbers)

sort_numbers = sorted(numbers, key=lambda x: -x) # for descending order
print(sort_numbers)

even_numbers = list(filter(lambda x: x%2 == 0, numbers))
print(even_numbers)

squared_numbers = list(map(lambda x: x*x, numbers))
print(squared_numbers)


#---------------calculator cli-----------------
def add(a, b):
    return a+b
    

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b== 0:
        return "Error: Division by zero"
    return a / b

def power(a, b):
    return a ** b

def modulo(a, b):
    if b == 0:
        return "Error: Modulo by zero"
    return a % b

def calculate(a, operation, b):
    # call the right function based on operation string
    # hint: use a dictionary mapping operation names to functions
    # this is cleaner than a long if/elif chain
    operations = {
        "add": add,
        "subtract": subtract,
        "multiply": multiply,
        "divide": divide,
        "power": power,
        "modulo": modulo
    }
    function = operations.get(operation)
    if function is None:
        return "Error: Unknown operation"
    return function(a, b)


def main():
    print("=== Calculator CLI ===")
    print("Operations: add, subtract, multiply, divide, power, modulo")
    print("Type 'quit' to exit")
    while True:
        user_input = input("Enter calculation (e.g. '5 add 3'): ")
        if user_input.lower() == "quit":
            print("Goodbye!")
            break
        try:
            a_str, operation, b_str = user_input.split()
            a = float(a_str)
            b = float(b_str)
            result = calculate(a, operation, b)
            print(f"Result: {result}")
        except ValueError:
            print("Invalid input format. Please enter in the format 'number operation number'.")

main()