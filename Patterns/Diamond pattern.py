n= 5
#upper half of diamond
for i in range(n):
    #Print spaces
    print(" " *(n - i - 1), end="")
    #Print Stars
    print("*" * (2 * i + 1))
#Other half of diamond
for i in range(n - 2 , - 1 , - 1):
   #Print spaces
    print(" " * (n - i - 1), end="")
    #Print Stars
    print("*" * (2 * i + 1))
   
