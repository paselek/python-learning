from car import *

car1 = Car("Toyota", "Camry", 2020)
car2 = Car("Honda", "Civic", 2019)
car1.display_info()
car2.display_info()
print(f"Total number of cars: {Car.number_of_cars}")