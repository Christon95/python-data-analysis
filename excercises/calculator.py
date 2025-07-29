def calculator():
    print("Select operation: +, -, *, /")
    operation = input("Operation: ")
    
    a = int(input("Enter first number: "))
    b = int(input("Enter second number: "))
    
    if operation == "+":
        print("Result:", a + b)
    elif operation == "-":
        print("Result:", a - b)
    elif operation == "*":
        print("Result:", a * b)
    elif operation == "/":
        try:
            print("Result:", a / b)
        except ZeroDivisionError:
            print("Error: Division by zero.")
    else:
        print("Invalid operation.")

calculator()
