string = "1234567890"

for char in string:
    print(char)


print('\n')
my_iterator = iter(string)
print(my_iterator)
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))
print(next(my_iterator))



print('\n')
string = "1234567890"
for char in iter(string):
    print(char)



print('\n')
my_list = ['Mon','Tue','Wed','Thrus','Fri','Sat','Sun']

my_iter = iter(my_list)


for char in range(0,len(my_list)):
    next_iter = next(my_iter)
    print(next_iter)

