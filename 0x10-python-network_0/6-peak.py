#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers."""


def find_peak(list_of_integers):
    """Finds the peak"""

    if list_of_integers == []:
        return None

    if len(list_of_integers) == 1:
        return list_of_integers[0]
    elif len(list_of_integers) == 2:
        return max(list_of_integers)

    mid = len(list_of_integers) // 2
    peak = list_of_integers[mid]
    if peak > list_of_integers[mid - 1] and peak > list_of_integers[mid + 1]:
        return peak
    elif peak < list_of_integers[mid - 1]:
        return find_peak(list_of_integers[:mid])
    else:
        return find_peak(list_of_integers[mid + 1:])
