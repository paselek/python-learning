#while loop execute code as long as condition is true

name = input("Enter your name: ")

while name == "":
    print("You did not enter your name. Please try again.")
    name = input("Enter your name: ")

print(f"Hello, {name}!")

food = input("What is your favorite food?(q to quit): ")

while food != "q":
    print(f"{food} is a great choice!")
    food = input("What is your favorite food?(q to quit): ")

print("Goodbye!")

num = int(input("Enter a number between 1 and 10 thats not 5: "))

while num == 5 or num < 1 or num > 10:
    print("Invalid input. Please try again.")
    num = int(input("Enter a number between 1 and 10 thats not 5: "))

print(f"You entered {num}.")