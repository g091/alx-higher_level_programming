#!/usr/bin/python3
value = ''
for letter in range(122, 96, -1):
    if letter % 2 == 0:
        value = value + chr(letter)
    else:
        value = value + chr(letter - 32)
print('{}'.format(value), end='')
