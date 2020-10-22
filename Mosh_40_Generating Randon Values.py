import random

for i in range(3):
    print(random.random())


# Another Method
print('\n')
for i in range(3):
    print(random.randint(10,20))


# Another Methods
print('\n')
members = ['John', 'Bob', 'Mery','Mosh']
leader = random.choice(members)
print(leader)