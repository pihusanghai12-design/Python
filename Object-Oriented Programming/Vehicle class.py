class Vehicle:
    def __init__(self, max_speed, mileage):
        self.max_speed= max_speed
        self.mileage= mileage
model= Vehicle(230, 23)     

print("Max. Speed= ", model.max_speed)
print("Mileage= ", model.mileage)