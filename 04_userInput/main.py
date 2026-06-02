# input() os a function that prompt the user to enter data
# the data is stored as a string

name = input("What is your name?: ")
age = int(input("How old are you?: "))

age += 1

print(f"Hello {name}!")
print("HAPPY BIRTHDAY!")
print(f"You are {age} years old")

#Exercise 1 Rectangle area calc

length = float(input("Enter the length of the rectangle: "))
width = float(input("Enter the width of the rectangle: "))
area = length * width
print(f"The area of the rectangle is: {area}")