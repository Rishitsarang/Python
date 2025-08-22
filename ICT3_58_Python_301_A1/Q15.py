# 15. Write a Python program for a Car Show room that sells cars of different brans of different price.
# Consider all features of a car and develop an OOP program that has following functionalities:

# 1. View the currently available cars in the showrroom
# 2. Display details of a car
# 3. Sell a car
# 4. Buy a car

# Use OOPs, Python data structures and various libraries like numpy,pandas.

# Implement exception handling in at least one script.

class Car:
    def __init__(self, brand, model, year, price, color):
        self.brand = brand
        self.model = model
        self.year = year
        self.price = price
        self.color = color
    
    def display_details(self):
        print(f"Brand: {self.brand}")
        print(f"Model: {self.model}")
        print(f"Year: {self.year}")
        print(f"Price: ${self.price}")
        print(f"Color: {self.color}")
        print("-" * 30)

class Showroom:
    def __init__(self):
        self.cars = []
    
    def view_cars(self):
        if not self.cars:
            print("No cars available in the showroom.")
            return
        print("Available Cars:")
        for idx, car in enumerate(self.cars):
            print(f"{idx + 1}. {car.brand} {car.model} ({car.year}) - ${car.price}")
        print()
    
    def display_car_details(self, index):
        if 0 <= index < len(self.cars):
            print("Car Details:")
            self.cars[index].display_details()
        else:
            print("Invalid car index.")
    
    def sell_car(self, index):
        if 0 <= index < len(self.cars):
            car = self.cars.pop(index)
            print(f"Sold car: {car.brand} {car.model} for ${car.price}")
        else:
            print("Invalid car index. Cannot sell.")
    
    def buy_car(self, brand, model, year, price, color):
        new_car = Car(brand, model, year, price, color)
        self.cars.append(new_car)
        print(f"Added new car: {brand} {model} ({year}) - ${price}")


showroom = Showroom()

showroom.buy_car("Toyota", "Camry", 2020, 24000, "Red")
showroom.buy_car("Honda", "Civic", 2019, 22000, "Blue")
showroom.buy_car("Ford", "Mustang", 2021, 35000, "Black")

showroom.view_cars()

showroom.display_car_details(1)

showroom.sell_car(0)

showroom.view_cars()
