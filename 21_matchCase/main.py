#match case is a new feature in python 3.10 it is similar to switch case in other languages. It allows you to match a value against a pattern

def day_of_week(day):
    match day:
        case 1:
            return "Monday"
        case 2:
            return "Tuesday"
        case 3:
            return "Wednesday"
        case 4:
            return "Thursday"
        case 5:
            return "Friday"
        case 6:
            return "Saturday"
        case 7:
            return "Sunday"
        case _:
            return "Invalid day"
        
print(day_of_week(1))
print(day_of_week(5))
print(day_of_week(8))