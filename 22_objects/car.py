class Car:
    number_of_cars = 0
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        Car.number_of_cars += 1

    def display_info(self):
        print(f"{self.year} {self.make} {self.model}")

    @classmethod
    def get_number_of_cars(cls):
        return cls.number_of_cars