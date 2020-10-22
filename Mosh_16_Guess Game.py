secret_number = 9
guess_count  = 0
guess_limit = 3

print('Guess Limit is 3')
while guess_count < guess_limit:
    guess = int(input('Guess: '))
    guess_count +=1

    if guess_count == 3:
        print('You faild in the Guess game.')
    elif guess == secret_number:
        print('You Win!')
        break
