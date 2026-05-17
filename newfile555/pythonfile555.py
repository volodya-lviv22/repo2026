def add(a, b):
    return a + b

def subtract(a, b):
    return a - b

def multiply(a, b):
    return a * b

def divide(a, b):
    if b == 0:
        return "Error: Division by zero"
    return a / b

def calculator():
    print("Simple Math Calculator")
    print("Operations: +, -, *, /")
    
    while True:
        try:
            num1 = float(input("Enter first number: "))
            operation = input("Enter operation (+, -, *, /): ")
            num2 = float(input("Enter second number: "))
            
            if operation == "+":
                print(f"Result: {add(num1, num2)}\n")
            elif operation == "-":
                print(f"Result: {subtract(num1, num2)}\n")
            elif operation == "*":
                print(f"Result: {multiply(num1, num2)}\n")
            elif operation == "/":
                print(f"Result: {divide(num1, num2)}\n")
            else:
                print("Invalid operation\n")
        except ValueError:
            print("Invalid input. Please enter numbers.\n")

if __name__ == "__main__":
    calculator()