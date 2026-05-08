print("Select your Ride: ")
print(" 1. Bike")
print("2. Car")

choice= int(input("Enter your ride here: "))

if choice == 1:
    print("Choose the type of Bike")
    print("1. Activa")
    print("2. Scooter")
    choice2= int(input("Enter your choice: "))
    if choice2 == 1:
        print("You have selected Activa.")
    else:
        print("You have selected Scooter.")  

elif choice == 2:
    print("Choose the type of Car")
    print("1. Tata")
    print("2. Suzuki")
    choice3= int(input("Enter your choice: "))
    if choice3 == 1:
        print("You have selected Tata.")
    else:
        print("You have selected Suzuki.")    

else:
    print("Invalid input")        

