try:
    num1, num2=eval(input("Enter any two numbers separated by a comma: "))
    result= num1/ num2
    print("Result is: ",result)
except ZeroDivisionError:
    print("Division by Zero is not allowed.")    
except SyntaxError:
    print(", is missing. Enter a number separated by comma.")   
except:
    print("Wrong input.")
else: 
    print("No Exceptions.")         
finally:
    print("This statement will always be printed. ")    