class Vehicle:
    def __init__(self, brand, max_speed):
        self.brand = brand
        self.max_speed = max_speed

    def show_detail(self):
        print("Brand: ",self.brand)
        print("Max Speed: ",self.max_speed)

class car(Vehicle):
    def __init__(self, model, seat, brand, max_speed):
        self.model= model
        self.seat= seat
        super().__init__(brand, max_speed)   

    def show_details(self):
        print("Model: ",self.model)
        print("Seat: ",self.seat)
        super().show_detail()

    def fuel(self, fuel):
        print("Fuel Type: ",fuel)

Car= car("BMW", 5, "BMW", 250)    
Car.show_detail()
Car.fuel("Petrol")

print("Is car instance of Vehicle? ", issubclass(car, Vehicle))