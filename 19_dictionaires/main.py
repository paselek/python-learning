#dictionaires are a collection of key value pairs {key:value}
#ordered and changable no duplicate keys but values can be duplicate

capitals = {"USA": "Washington DC", "India": "New Delhi", "China": "Beijing", "Russia": "Moscow"}

print(capitals)
print(capitals.get("India")) #accessing the value of a key
capitals["India"] = "Delhi" #changing the value of a key
print(capitals)
capitals["France"] = "Paris" #adding a new key value pair or capitals.update({"France": "Paris"}) #another way to add or update a new key value pair
print(capitals)
del capitals["Russia"] #removing a key value pair or capitals.pop("Russia") #another way to remove a key value pair
print(capitals)

if capitals.get("Japan"):
    print("That capital exists")
else:
    print("That capital does not exist")

print(capitals.keys()) #getting all the keys in the dictionary
print(capitals.values()) #getting all the values in the dictionary

for key, value in capitals.items(): #looping through the dictionary
    print(f"{key} : {value}")
