'''
if name is less then 3 then 3 characters long
    name must be at least 3 characters
otherwaise if it's more then 50 characters long
    name can be a maximum of 50 characters
otherwaise
    name looks goods!
'''
print('Enter Characters: ')
name = input()

if len(name) <3:
    print('name must be at least 3 characters')
elif len(name) >50:
    print('name can be a maximum of 50 characters')
else:
    print('name looks goods!')