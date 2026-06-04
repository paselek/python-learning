#for loop will execute a block of code a certain number of times

for x in range(5):
    print(x) #prints 0,1,2,3,4
print()
for x in range(2,10,2):
    print(x) #prints 2,4,6,8
print()
credit_card_number = "1234-5678-9012-3456"

for x in credit_card_number:
    if x == "-":
        continue
    print(x, end="")
print()

credits = [100, 200, 300, 400, 500]

for credit in credits:
    if credit == 300:
        break
    print(credit) #prints 100,200