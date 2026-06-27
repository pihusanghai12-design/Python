import random
choices=["rock", "paper", "scissors"]
user= input("Enter rock, paper, or scissors: ")
computer= random.choice(choices)
print(f"User's choice is {user} and computer's choice was {computer}")
if user==computer:
    print("Its a tie")
elif (user == 'rock' and computer=='scissors')or (user == 'paper' and computer=='rock') or (user == 'scissors' and computer=='paper'):
     print("You win")
else:
     print("You lose")     
