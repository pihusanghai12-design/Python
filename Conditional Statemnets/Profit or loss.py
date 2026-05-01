Sp=int(input("Enter the selling price of your product: "))
Cp= int(input("Enter the cost price of your product: "))
if Sp > Cp:
    print("You have got a profit of ", Sp-Cp)
else:
    print("You have got a loss of ", Cp-Sp)    