from random import randint
num1 = randint(1,101)
num2 = randint(1,101)
grade = 0
num = 0

sum = num1 + num2

while num != sum:
    print("Enter the answer to ", num1, "+", num2, " or press 's' to skip ")
    user_input = input()
    
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != sum:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1
        break

print('Next Question....')

num1 = randint(1,101)
num2 = randint(1,101)
num = 0

sum = num1 + num2

while num != sum:
    print("Enter the answer to ", num1, "+", num2, " or press 's' to skip ")
    user_input = input()
    
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != sum:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1
        break

print('Next Question....')

num1 = randint(1,101)
num2 = randint(1,101)
num = 0

sum = num1 + num2

while num != sum:
    print("Enter the answer to ", num1, "+", num2, " or press 's' to skip ")
    user_input = input()
    
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != sum:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1
        break

print('Next Question....')

num1 = randint(1,101)
num2 = randint(1,101)
num = 0

sum = num1 + num2

while num != sum:
    print("Enter the answer to ", num1, "+", num2, " or press 's' to skip ")
    user_input = input()
    
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != sum:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1
        break

print('Next Question....')




print("You received grade of: ",grade /4 * 100 ) 

