class Pets:
    print("Welcome to the Pet profile builder.")
    print()

    def __init__(self, name, age, breed, color):
        self.name = name
        self.age = age
        self.breed = breed
        self.color = color

pet1 = Pets("Max", 6, "Golden Retriever", "Golden")
pet2 = Pets("Bella", 3, "Labrador", "Black")

print("Profile of pet 1:")
print("Pet 1 name is:", pet1.name)
print("Pet 1 age is:", pet1.age)
print("Pet 1 breed is:", pet1.breed)
print("Pet 1 color is:", pet1.color)
print()
print("Profile of pet 2:")
print("Pet 2 name is:", pet2.name)
print("Pet 2 age is:", pet2.age)
print("Pet 2 breed is:", pet2.breed)
print("Pet 2 color is:", pet2.color)
