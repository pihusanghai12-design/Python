try:
    number=float(input("Enter any number: "))
    print("The number you entered is: ",number)
except ValueError as a:
    print("Exception: ",a)    