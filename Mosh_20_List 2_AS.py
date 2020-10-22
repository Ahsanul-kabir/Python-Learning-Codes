# Write a program to find the largest number in a list.

numbers = [2,25,6,5,1]

# print(max(numbers))
max = numbers[0]

for number in numbers:
    if number > max:
        max = number
print(max)