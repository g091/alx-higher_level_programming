#!/usr/bin/python3
def weight_average(my_list=[]):
    if len(my_list) == 0:
        return 0
    else:
        return (sum(a * b for a, b in my_list) / sum(b for a, b in my_list))
