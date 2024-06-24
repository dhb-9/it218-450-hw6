## original
# using python main.py # # operation
'''
from decimal import Decimal, InvalidOperation
import sys
from calculator import Calculator


def calculate(a, b, operation_name):
    operation_mappings = {
    'add': Calculator.add,
    'subtract': Calculator.subtract,
    'multiply': Calculator.multiply,
    'divide': Calculator.divide
    }
        
    try:
        a_dec = Decimal(a)
        b_dec = Decimal(b)
        result = operation_mappings.get(operation_name)
        if result:
            print(f"The result of {a} {operation_name} {b} is equal to {result(a_dec, b_dec)}")
        else:
            print(f"Unknown operation: {operation_name}")
    except InvalidOperation:
        print(f"Invalid number input: {a} or {b} is not a valid number.")
    except Exception as e:
        if (b_dec == 0):
            print ("An error occurred: Cannot divide by zero")
        else:
            print ("An error occurred: {e}")

def main():
    if len(sys.argv) != 4:
        print("Usage: python main.py <number1> <number2> <operation>")
        sys.exit(1)
    
    _, a, b, operation = sys.argv
    calculate(a, b, operation)

if __name__ == '__main__':
    main()
'''
## for app/command pattern
# using python main.py
from app import App    

if __name__ == "__main__":
    App.start()
