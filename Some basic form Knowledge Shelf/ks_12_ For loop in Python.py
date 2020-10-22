for i in range(20,1,-2):
    print('i is now {}'.format(i))




number = '9,223,372,036,854,775,807'

for i in range(0,len(number)):
    print(number[i])





number = '9,223,372,036,854,775,807'
print(type(number))
for i in range(0,len(number)):
    if number[i] in '0123456789':
        print(number[i],end='')





number = '9,223,372,036,854,775,807'
cleanedNumber = ''

for i in range(0, len(number)):
    if number[i] in '0123456789':
        cleanedNumber = cleanedNumber + number[i]

newNumber = int(cleanedNumber)
print('\n')
print(type(newNumber))
print("The number is {}".format(newNumber))