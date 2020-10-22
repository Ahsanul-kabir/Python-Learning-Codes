
numbers = [5, 2, 7, 1, 7, 4]
numbers.append(20)
print(numbers)

print('\n')
numbers.insert(2,15)
print(numbers)

print('\n')
numbers.remove(7)
print(numbers)

"""
print('\n')
numbers.clear()  #clear all numbers
print(numbers)

"""

print('\n')
numbers.pop()
print(numbers)

print('\n')
print(numbers.index(15))

# Another Method
print('\n')
print(50 in numbers)

print('\n')
print(numbers.count(7))

print('\n')
numbers.sort()
print(numbers)

print('\n')
numbers.reverse()
print(numbers)


print('\n')
numbers2 = numbers.copy()
numbers.append(11)
print(numbers)
print(numbers2)

