#Typecasting is the process of converting a variable from one data type to another.
# str(), int(), float(), bool()

name = "Pawel"
age = 25
height = 1.8
is_graduate = True
print("Before typecasting age:")
print(type(age)) # <class 'int'>
print("After typecasting age:")
print(type(str(age))) # <class 'str'>
print("Age to float:")
print(float(age)) # 25.0
print("Height to integer:")
print(int(height)) # 1

print("Is graduate to string:")
print(str(is_graduate)) # True
print("Is graduate to integer:")
print(int(is_graduate)) # 1

print("Name to boolean:")
print(bool(name)) # True
print("Empty string to boolean:")
print(bool("")) # False