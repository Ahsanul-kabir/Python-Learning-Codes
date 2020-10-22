'''
>help :
 start - to start the car
 stop - to stoop the car
 quit - to exit

 jhhkjh:
 I don't understand that...

 start:
 Car started.. Reddy to go!

 stop:
 Car stopped.

'''
commamd = input('Enter Command: ')
if commamd == 'help':
    print('start - to start the car \nstop - to stoop the car \nquit - to exit ')

elif commamd == 'start':
    print('Car started.. Reddy to go!')
elif commamd == 'quit':
    print('Car stopped.')