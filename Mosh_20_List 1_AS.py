# Find numbers of words
# Find numbers of latters
# Find numbers of degits

num_of_words = 0
num_of_letters = 0
num_of_degits = 0

input = input('Enter some thing as you wish : ')
data = input.lower()
for x in data:
    if x >= 'a' and x <='z':
        num_of_letters = num_of_letters + 1

    elif x >= '0' and x <='9':
        num_of_degits = num_of_degits + 1

    elif x == ' ':
        num_of_words = num_of_words + 1

print(num_of_letters)
print(num_of_degits)
print(num_of_words + 1)