#indexing is accesing elements of a sequence by using [] 
# [start:end:step]

credit_card_number = "1234-5678-9012-3456"

print(credit_card_number[0]) #1
print(credit_card_number[5]) #5
print(credit_card_number[0:4:1]) #1234
print(credit_card_number[:4]) #1234
print(credit_card_number[5:9:1]) #5678

last_digits = credit_card_number[-4:]
print(f"XXXX-XXXX-XXXX-{last_digits}") #3456

print(credit_card_number[::-1]) #reversing string