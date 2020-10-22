'''
xxxxx
xx
xxxxx
xx
xx
'''

numbers = [5,2,5,2,2]
#for x_count in numbers:
   # print('x' * x_count)
#print('\n')

for x_count in numbers:
    output = ''
    for count in range (x_count):
        output = output + 'x'
        print(output)