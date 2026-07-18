Starting_value= int(input("Enter your starting value: "))
Last_value= int(input("Enter your ending value: "))

even= []
odd= []

for n in range(Starting_value, Last_value + 1):
    if n % 2==0:
        even.append(n)
    else:
        odd.append(n)

print("Even numbers: ",even)
print("Odd numbers: ",odd)        
