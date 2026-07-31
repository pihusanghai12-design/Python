#List Comprehension
items=["Pen","Eraser","sharpener","ruler"]
items_length= [item for item in items if item!="ruler"]
print(items_length)

#Dictonary Comprehension
items= ["Pencil","Copy"]
stock_counts=[0,12]
inventory= {item:count for item, count in zip(items,stock_counts)}
print(inventory)

#map function
numbers=[2,3,4,5]
def cubed(x):
    return x ** 3

cube= map(cubed,numbers)
print(tuple(cube))

#exit function
print("Program starts")
x=5
if x <10:
    print("x is too small, exiting..")
    exit()

print("This line will not continue")    