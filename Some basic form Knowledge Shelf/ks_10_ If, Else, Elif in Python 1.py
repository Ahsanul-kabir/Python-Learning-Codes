print("Please guess a number b/w 1 to 10")
guess = int(input())

if guess < 5:
    print("Please guess higher")

    guess = int(input())
    if guess == 5:
        print("Well done, your guess is correct!!")
    else:
        print("Sorry, you have not not guessed the correct number")
elif guess > 5:
    print("Please guess lower")

    guess = int(input())
    if guess == 5:
        print("Well done, your guess is correct!!")
    else:
        print("Sorry, you have not not guessed the correct number")
else:
    print("You got it first time")