while True:
    print('Who are you?')
    name = input()

    if name != 'vishwajeet':
        continue

    print("Hello, vishwajeet. what is your password'It is a fish'")
    password = input()
    if password == 'swordfish':
        break
print('Congrats!!!, Access Granted')