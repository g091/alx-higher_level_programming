#!/usr/bin/python3
def uppercase(str):
    result = ''
    for letter in str:
        index = ord(letter)
        if index >= 97 and index <= 122:
            result += chr(index - 32)
        elif index >= 65 and index <= 90:
            result += chr(index)
        else:
            result += chr(index)
    print('{}'.format(result))
