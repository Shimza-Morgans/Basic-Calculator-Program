# Basic Calculator Program

# Function to perform the calculation
def calculator():
    # Ask the user to input two numbers and an operation
    num1 = float(input("Enter the first number: "))
    num2 = float(input("Enter the second number: "))
    operation = input("Enter the operation (+, -, *, /): ")

    # Perform the calculation based on the user's input
    if operation == "+":
        result = num1 + num2
    elif operation == "-":
        result = num1 - num2
    elif operation == "*":
        result = num1 * num2
    elif operation == "/":
        if num2 != 0:
            result = num1 / num2
        else:
            result = "Error! Division by zero."
    else:
        result = "Invalid operation!"

    # Print the result
    print(f"{num1} {operation} {num2} = {result}")

# Call the function to run the calculator
calculator()
