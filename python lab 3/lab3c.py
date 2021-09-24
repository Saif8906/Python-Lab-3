

sum = 0
print("Summing Calculator")

while  True:
    print("The sum so far = ", str(sum))
    user_input = input("Enter a number to add to your sum. Pressing Enter would exit. ")
    if user_input == "":
        break
    else:
        sum += int(user_input)

print("Thank you for using summing calculator. The final sum was ",str(sum), ".")
