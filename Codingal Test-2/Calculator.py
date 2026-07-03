def add(a,b):
    return a+b
def sub (a,b):
    return a-b
def multiply(a,b):
    return a*b
def divide(a,b):
    if b==0:
        return "Error. Division by Zero."
    return a/b 

print("Choose which operation you want to apply:")
print("a. Add")
print("b. Subtract")
print("c. Multiply")
print("d. divide")

choice= input("Enter your operation here  a/ b/ c/ d:  ")

try:
    num1= float(input("Enter the first number: "))
    num2= float(input("Enter the second number: "))
    if choice == "a":
        print("Addition of the two numbers: ", add(num1, num2))
    elif choice == "b":
        print("Subtraction of the two numbers: ", sub(num1, num2))  
    elif choice == "c":
        print("Multiplication of the two numbers: ", multiply(num1, num2))  
    elif choice == "d":
        print("Division of the two numbers: ", divide(num1, num2))  
    else:
        print("Invalid input.")    
except ValueError:
    print("Invalid numbers. ")        








