#if = Do something if a condition is true
#else = Do something if the condition is false
age = int(input("How old are you? "))
if age>=100:
    print("You are old enough to vote, but you are very old!")
elif age >= 18:
    print("You are old enough to vote!")
elif age<0:
    print("You haven't been born yet!")
else:
    print("You are not old enough to vote.")

response = input("Would you like to hear a joke? (Y/N) :")

if response.upper() == "Y":
    print("What do you call a bear with no teeth? A gummy bear!")
elif response.upper() == "N":
    print("Okay, maybe next time!")
else:
    print("Invalid response. Please enter Y or N next time.")

for_sale = True
if for_sale:
    print("This item is for sale!")
else:    
    print("This item is not for sale.")