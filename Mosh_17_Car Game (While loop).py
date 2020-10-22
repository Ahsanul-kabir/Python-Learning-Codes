'''
>help :
 start - to start the car
 stop - to stoop the car
 quit - to exit

 jhhkjh:
 I don't understand that...

 start:
 Car started.. Ready to go!

 stop:
 Car stopped.

'''
command = ''
started = False


while True:
    command = input('>').lower()

    if command == 'start':
        if started is True:
            print('Car is already started.')
        else:
             started = True
             print('Car started.')
    elif command == 'stop':
        if not started:
            print('Car is already stoped!')
        else:
           started = False
           print('Car Stopped')


    elif command == 'help':
        print('''
start - to start the car
stop - to stoop the car
quit - to exit
        ''')
    elif command == 'quit':
        break

    else:
        print("Sorry I don't understand you.")



