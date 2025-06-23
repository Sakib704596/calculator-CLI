def add(a, b):
    return a + b
def sub(a, b):
    return a - b
def mul(a, b):
    return a * b
def div(a, b):
    if b == 0:
        return "Cannot divide by zero!"
    return a / b
while True:
    print("\n--- Simple Calculator ---")
    print("Type 'exit' to quit.")
    
    user_input = input("Enter first number (or 'exit'): ")
    if user_input.lower() == "exit":
        print("Calculator exited.")
        break
    num1 = int(user_input)

    user_input = input("Enter second number: ")
    if user_input.lower() == "exit":
        print("Calculator exited.")
        break
    num2 = int(user_input)

    op = input("Enter operator (+, -, *, /): ")

    if op == "+":
        print("Result:", add(num1, num2))
    elif op == "-":
        print("Result:", sub(num1, num2))
    elif op == "*":
        print("Result:", mul(num1, num2))
    elif op == "/":
        print("Result:", div(num1, num2))
    else:
        print("Invalid operator! Please try again.")
