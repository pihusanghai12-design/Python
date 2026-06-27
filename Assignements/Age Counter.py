try:
    age=int(input("enter your age: "))
    if (age <=18):
        raise ValueError
    else:
        print("You are eligible for voting.")
       
          
except ValueError:
    print("You are not eligible.")          
        
if age % 2 ==0:
            print("It is an even age.")
else:
            print("It is an odd age.")  
