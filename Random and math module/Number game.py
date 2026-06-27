import random
number=str(random.randint(0,9))
print("I will generate a number from 0 to 9 and you have to guess the number one digit at at time.")
print('The game ends when you get 1 hero.')
while True:
    guess= (input("Enter your guess number: "))
    if number == guess:
        print("You won the game.")
        print("The number was: ",number)
        break
    else:
        print('The guess is not right. Try again!')