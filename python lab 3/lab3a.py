num = 0
grade = 0

while num != 26:
    user_input = input("Enter the answer to 12 + 14 or press 's' to skip ")
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != 26:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1

print('Next Question....')

while num != 31:
    user_input = input("Enter the answer to 23 + 8 or press 's' to skip: ")
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != 31:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1

print('Next Question....')

while num != 43:
    user_input = input("Enter the answer to 30 + 13 or press 's' to skip ")
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != 43:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1

print('Next Question....')

while num != 44:
    user_input = input("Enter the answer to 17 + 27 or press 's' to skip ")
    if user_input == 's':
        break
    else:
        num = int(user_input)
    
    if num != 44:
        print("Incorrect. Try again")
    else:
        print("Correct! You have been awarded 1 point!")
        grade = grade + 1


print("You received grade of: ",grade /4 * 100 ) 

