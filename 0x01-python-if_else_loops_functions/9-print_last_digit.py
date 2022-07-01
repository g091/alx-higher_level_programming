#!/usr/bin/python3
def print_last_digit(digit):
    if digit < 0:
        last_digit = ((digit * -1) % 10)
    else:
        last_digit = digit % 10
    print('{}'.format(last_digit), end="")
    return last_digit
