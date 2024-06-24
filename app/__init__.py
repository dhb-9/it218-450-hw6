from decimal import Decimal
from calculator.plugin_loader import load_plugins, get_plugin

class App:
    @staticmethod
    def start() -> None:
        print("Calculator App. Type 'exit' to exit.")
        
        load_plugins("calculator/commands")
        
        while True:
            user_input = input("Enter command (add/subtract/multiply/divide) or 'exit' to quit: ")
            if user_input.lower() == "exit":
                print("Exiting...")
                break

            try:
                if user_input in ('add', 'subtract', 'multiply', 'divide'):
                    a = Decimal(input("Enter first number: "))
                    b = Decimal(input("Enter second number: "))
                    
                    command_class = get_plugin(user_input)
                    if command_class:
                        command = command_class(a, b)
                        result = command.execute()
                        print(f"Result: {result}")
                    else:
                        print(f"Command '{user_input}' not found.")
                else:
                    print("Unknown command.")
            except Exception as e:
                print(f"Error: {e}")
