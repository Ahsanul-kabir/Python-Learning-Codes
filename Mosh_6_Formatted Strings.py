first = 'John'
last = 'Smith'
message = first + ' [' + last + '] is a coder'
print(message)

print('\n')
message1 = "{} [{}] is a coder" .format(first,last)
print(message1)

print('\n')
message2 = f"{first} [{last}] is a coder"
print(message2)