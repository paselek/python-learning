#collection is a data structure that can hold multiple items in a single variable.
#list [] ordered, changeable, allows duplicate
mylist = ["apple", "banana", "cherry"]
print(mylist)
print(mylist[0]) #accessing the first item in the list
print(mylist[::-1]) #accessing the second item in the list
for fruit in mylist: #looping through the list
    print(fruit)
print(len(mylist)) #length of the list
print("apple" in mylist) #check if an item is in the list
mylist.append("orange") #add an item to the end of the list
mylist.insert(1, "grape") #add an item at a specific position
mylist.remove("banana") #remove an item from the list
mylist.reverse() #reverse the order of the list
mylist.sort() #sort the list in ascending order
print(mylist)
print(mylist.index("cherry")) #find the index of an item in the list
#set {} unordered, unchangeable (but remove/add OK), no duplicate
myset = {"apple", "banana", "cherry"}
myset.add("orange") #add an item to the set
myset.remove("banana") #remove an item from the set
print(myset)
#tuple () ordered, unchangeable, allows duplicate
mytuple = ("apple", "banana", "cherry")
print(mytuple)