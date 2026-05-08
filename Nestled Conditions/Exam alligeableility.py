medical_cause=input("Did you have any medical cause(Yes/No): ")
if medical_cause=="Yes":
    print("You are not allowed.")
else: 
    atten=int(input("Enter your attendance: "))
    if atten >=75:
        print('You are allowed to give your examination.')
    else:
        print("You are not allowed.")    
