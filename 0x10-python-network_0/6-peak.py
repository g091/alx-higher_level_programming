#!/usr/bin/python3
"""Function that finds a peak in a list of unsorted integers"""


def find_peak(list_of_integers):
    """Finds the peak"""

    A = list_of_integers[:]
    if A == []:
        return None

    def recursive(A, left=0, right=len(A) - 1):
        """Recursive function"""

        mid = (left + right) // 2
        if ((mid == 0 or A[mid - 1] <= A[mid]) and
                (mid == len(A) - 1 or A[mid + 1] <= A[mid])):
            return A[mid]
        if mid - 1 >= 0 and A[mid - 1] > A[mid]:
            return recursive(A, left, mid - 1)
        return recursive(A, mid + 1, right)
    return recursive(A)
