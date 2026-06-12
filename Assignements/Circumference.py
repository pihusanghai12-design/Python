def area(r):
    return 3.14 * r* r
def circumference(r):
    return 2* 3.14* r

print("Please select the operation: ")
print("a. Area")
print("b. Circumference")

choice= input("Enter the selected option ( a/ b): ")

radius= int(input("Enter the radius of the circle of your own choice: "))

if choice == "a":
    print("Area of the circle is :", area(radius))
elif choice == "b":
    print("The circumference of the circle is: ", circumference(radius))    
else: 
    print("This is an invalid input.")    