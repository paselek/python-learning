name = input("Enter your name: ")

# String concatenation
greeting = "Hello, " + name + "!"
print(greeting)
# String formatting using f-strings
greeting = f"Hello, {name}!"
print(greeting)
# String methods
print(name.upper())  # Convert to uppercase
print(name.lower())  # Convert to lowercase
print(name.capitalize())  # Capitalize the first letter
print(name.replace("a", "o"))  # Replace 'a' with 'o'
print(name.split())  # Split the name into a list of words
print(name.strip())  # Remove leading and trailing whitespace
print(len(name))  # Get the length of the name
print(name.find("a"))  # Find the index of the first occurrence of 'a'
print(name.rfind("A"))  # Find the index of the last occurrence of 'A'
print(name.count("a"))  # Count the number of occurrences of 'a'
print(name.startswith("A"))  # Check if the name starts with 'A'
print(name.endswith("n"))  # Check if the name ends with 'n'
print(name.isalpha())  # Check if the name contains only letters
print(name.isdigit())  # Check if the name contains only digits
print(name.isalnum())  # Check if the name contains only letters and digits
print(help(str))  # Get a list of all string methods and their descriptions
