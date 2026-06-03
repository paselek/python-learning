#conditional expressions, also known as ternary operators, allow you to evaluate a condition and return a value based on the result in a single line of code.
#syntax: value_if_true if condition else value_if_false

age = 18
status = "Adult" if age >= 18 else "Minor"
print(status)  # Output: Adult