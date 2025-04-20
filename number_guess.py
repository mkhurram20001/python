import random

top_range = input("Enter a number: ")
if top_range.isdigit():
    top_range = int(top_range)
    if top_range <= 0:
        print("Please enter a number greater than 0.")
        quit()
else:
    print("Please enter a number next time.")
    quit()

random_number = random.randint(0, top_range)
print(f"Random number is {random_number}")

while True:
    user_guess = input("Enter a number: ")
    if user_guess.isdigit():
        user_guess = int(user_guess)
    else:
        print("Your guess is wrong. Please try again")
        continue

    if user_guess == random_number:
        print("You got it!")
        break
    else:
        print("You guessed wrong.")
    