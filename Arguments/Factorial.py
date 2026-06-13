def factorial(x):
    '''This is a recursive function to find the factorial of a number'''
    if x==0 or x==1:
       return 1
    else:
       return x*factorial(x-1)
print(factorial.__doc__)    
print("The Factorial of 5 is: ",factorial(6))
    