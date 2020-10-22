myCat = {'size':'fat','color':'gray','disposition':'loud'}
print(myCat['color'])



print('\n')
spam1 =['cat','dog','rat']
spam2 =['dog','rat','cat']
print(spam1 == spam2)



print('\n')
myCat1 = {'size':'fat','color':'gray','disposition':'loud'}
myCat2 = {'color':'gray','disposition':'loud','size':'fat'}
print(myCat1 == myCat2)


print('\n')
spam = {'name':'vishwajeet','gender':'M','age':'29'}

for v in spam.values():
    print(v)



print('\n')
for k in spam.keys():
    print(k)



print('\n')
for i in spam.items():
    print(i)



print('\n')
birthdays = {'Rahul': 'Jan 1', 'Vivek': 'Aprl 21', 'vishwajeet': 'Aug 1'}

while True:
    print("Enter the name : ")
    name = input()
    if name == '':
        break

    if name in birthdays:
        print(birthdays[name] + ' is the birthday of ' + name)

    else:
        print('I do not have birthday info for ' + name)

        print('What is their birthday?')
        bday = input()
        birthdays[name] = bday
        print('Birthday database is updated')