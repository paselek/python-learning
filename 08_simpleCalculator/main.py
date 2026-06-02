#Calculator
number1 = float(input("Enter first number: "))
number2 = float(input("Enter second number: "))

operator = input("Enter operator (+, -, *, /): ")

if operator == "+":
    result = number1 + number2
elif operator == "-":
    result = number1 - number2
elif operator == "*":
    result = number1 * number2
elif operator == "/":
    if number2 != 0:
        result = round(number1 / number2, 3)
    else:
        result = "Error: Division by zero is not allowed."
else:
    result = f"Error: {operator} is an invalid operator."

print(f"The result is: {result}")