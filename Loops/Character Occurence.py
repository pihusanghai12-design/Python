string=input("Enter any word: ")
letter=input("Enter the letter you want to check: ")
i=0
count=0
while i <len(string):
    if string[i]==letter:
        count=count+1
    i=i+1
print("The total number of times ",letter,"has occured: ",count)        
