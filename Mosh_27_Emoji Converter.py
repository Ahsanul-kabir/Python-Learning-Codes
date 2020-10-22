
message = input(">")
words = message.split(' ') # String ke List e Convert kora
print(words)
print('\n')

emoji = {
 ":)" : "😀",
 ":(" : "😔"
}

output =""
for word in words:
    output = output + emoji.get(word, word) +" "
print(output)
