import random
secret_number= random.randint(1,5)
print("Guessing Secret Number Game")
number=int(input("Enter any number for guessing: "))
while number >=5:
    if number < secret_number:
        print("The number is 🧊 ")
    elif number > secret_number:
        print("The number is 🥶")   
    else:
        print("❤️")     