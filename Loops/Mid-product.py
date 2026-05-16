num=input("Enter a number: ")
if len(num) >=4:
    midIndex= len(num) //2
    midOne= int(num[midIndex-1])
    midTwo=int(num[midIndex])
    product= midOne*midTwo
    print(f"Product of Mid digits ({midOne} * {midTwo}) = {product}")
else:
    print("The number should be 4 or more than 4- digits.")    
