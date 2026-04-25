#Taking amount as input from user
amount=int(input("Enter your amount: "))

#Calculating the number of notes of different denominators
note1=amount//100
note2=(amount%100)//50
note3=((amount%100)%50)//10

print("notes of 100 rupees: ",note1)
print("notes of 50 rupees: ",note2)
print("notes of 10 rupees: ",note3)