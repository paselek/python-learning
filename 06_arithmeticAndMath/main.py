numbah = 1

numbah = numbah + 1
numbah += 1
numbah = numbah - 1
numbah -= 1
numbah = numbah * 2
numbah *= 2
numbah = numbah / 2
numbah /= 2
numbah = numbah ** 2 #numbah powered by 2
numbah **= 2
remainder = numbah % 3 #numbah divided by 3 and the remainder is stored in the variable remainder
numbah %= 3 #remainder is in numbah

print(numbah)

###################################

x = 3.14
y = -4
z = 5

result = round(x) #rounds x to the nearest whole number
result = round(x, 1) #rounds x to 1 decimal place
result = abs(y) #returns the absolute value of y (removes the negative sign)
result = pow(z, 2) #z to the power of 2
result = max(x, y, z, 2) #returns the largest value among x, y, and z and 2
result = min(x, y, z) #returns the smallest value among x, y, and z
print(result)

import math

print(math.pi) #prints the value of pi
print(math.e) #prints the value of e
print(math.sqrt(16)) #prints the square root of 16
print(math.ceil(3.14)) #rounds 3.14 up to the nearest whole number
print(math.floor(3.14)) #rounds 3.14 down to the nearest whole number

###########################
#Circumference of a circle = 2 * pi * radius
radius = float(input("Enter the radius of the circle: "))
circumference = 2 * math.pi * radius
print(f"The circumference of the circle is: {round(circumference, 2)}")

#Area of a circle = pi * radius^2
area = math.pi * pow(radius, 2)
print(f"The area of the circle is: {round(area, 2)}")

#Right angled triangle - Pythagorean theorem: a^2 + b^2 = c^2
print("To calculate the length of the hypotenuse of a right angled triangle, enter the lengths of the two sides.")
side_a = float(input("Enter the length of side a: "))
side_b = float(input("Enter the length of side b: "))
hypotenuse = math.sqrt(pow(side_a, 2) + pow(side_b, 2))
print(f"The length of the hypotenuse is: {round(hypotenuse, 2)}")
