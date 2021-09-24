from random import randint
secret  = randint(1,11)
user_guess = 0

while user_guess != secret:
    user_guess = int(input("Enter a number between 1 and 10: "))
    if user_guess == secret:
        print("Correct! You win")
        break
    else:
        print("Sorry, thats not it.")


        


