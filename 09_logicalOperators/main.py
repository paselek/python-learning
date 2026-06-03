#logical operators are used to combine conditional statements
#or - returns true if one of the statements is true
#and - returns true if both statements are true
#not - reverse the result, returns false if the result is true

a = 10
b = 20
if a > 5 and b > 15:
    print("Both conditions are true")
if a > 5 or b < 15:
    print("At least one condition is true")
if not a > 15:
    print("a is not greater than 15")
    