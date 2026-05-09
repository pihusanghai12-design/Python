n= int(input("Enter a number greater than 1: "))
print(f"Numbers from {n} to 1 are: ")
#Starts at n
#Stops just before 0 so it ends at 1
#Moves backwards with step -1
for i in range(n,0,-1):
    print(i)