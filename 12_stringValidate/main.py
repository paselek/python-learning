#validate user input for a username
#username must be between 5 and 15 characters long, can only contain letters and numbers
#username must not contain spaces

username = input("Enter a username: ")

if len(username)<5 or len(username)>15:
    print("Username must be between 5 and 15 characters long.")
elif username.isalnum() == False:
    print("Username can only contain letters and numbers.") #covers also spaces and special characters
else:
    print("Username is valid.")
