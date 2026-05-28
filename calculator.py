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