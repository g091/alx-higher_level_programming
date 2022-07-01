#!/usr/bin/python3
def common_elements(set_1, set_2):
    s1 = list(set_1)
    s2 = list(set_2)
    new_list = []
    for val in s1:
        for value in s2:
            if val == value:
                new_list.append(val)
    return set(new_list)
