#!/usr/bin/python3
def remove_char_at(str, n):
    printout = ''
    if n >= 0:
        str1 = str[:n]
        str2 = str[n + 1:]
        printout = str1 + str2
    else:
        printout = str
    return printout
