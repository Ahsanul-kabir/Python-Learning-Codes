
def emoji_Converter(message):
    words = message.split(' ')  # String ke List e Convert kora
    print(words)
    print('\n')

    emoji = {
        ":)": "😀",
        ":(": "😔"
    }

    output = ""
    for word in words:
        output = output + emoji.get(word, word) + " "
    return output


message = input(">")
print(emoji_Converter(message))
