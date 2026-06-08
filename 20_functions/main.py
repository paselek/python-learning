# function is a block of code which only runs when it is called. You can pass data, known as parameters, into a function. A function can return data as a result.
# creating a function

def my_function():
    print("Hello from a function")

my_function() # calling a function

def display_invoice(username, amount, due_date):
    print(f"Hello {username}")
    print(f"Your bill of ${amount} is due on {due_date}")

display_invoice("John", 100, "2024-07-01") # calling a function with arguments

def add(x,y):
    return x + y

result = add(5, 3)
print(result)

#default arguments are default value for a parameter if no argument is passed
#1. positional arguments, 2. keyword arguments, 3. default arguments, 4. arbitrary arguments

def greet(name, greeting="Hello", punctuation="!"):
    print(f"{greeting} {name}{punctuation}")
greet("Alice") # using default argument
greet("Bob", "Hi") # using positional argument
greet("Charlie", punctuation="?") # using keyword argument
greet("Dave","Hey",".") # using keyword argument

def add2(*args):
    return sum(args)
print(add2(1, 2, 3, 4, 5)) # using arbitrary arguments

def print_address(**kwargs):
    for key, value in kwargs.items():
        print(f"{key}: {value}")

print_address(street="123 Main St", city="Anytown", state="CA", zip="12345") # using arbitrary keyword arguments