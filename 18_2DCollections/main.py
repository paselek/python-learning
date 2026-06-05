fruits =        ["apple", "banana", "cherry", "orange", "grape"]
vegetables =    ["carrot", "broccoli", "tomato"]
meats =         ["chicken", "beef", "fish"]

groceries = [fruits, vegetables, meats] #2D list
groceries2 = [["apple", "banana", "cherry", "orange", "grape"], 
              ["carrot", "broccoli", "tomato"], 
              ["chicken", "beef", "fish"]] #2D list
print(groceries)
print(groceries[0]) #accessing the first list in the 2D list
print(groceries[0][0]) #accessing the first item in the first list
print(groceries[1][2]) #accessing the second item in the second list
print(groceries2[0][0]) #accessing the first item in the first list of groceries2
print(groceries2[1][2]) #accessing the second item in the second list of groceries2

for collection in groceries2:
    for item in collection:
        print(item, end=" ") #end=" " is used to print the items in the same line
    print() #print a new line after each collection

num_pad = [ (1, 2, 3),
            (4, 5, 6),
            (7, 8, 9),
            ("*", 0, "#")]

for row in num_pad:
    for num in row:
        print(num, end=" ")
    print()
