#!/usr/bin/env python

"""
Implement a function rotateArray(vector<int> arr, int r) which rotates the array by r places.
Eg 1 2 3 4 5 on being rotated by 2 gives 4 5 1 2 3.

Naive implementation: use extra space O(n), time O(n).

Follow up:
    Could you do it in-place?
"""


def rotate_array(array, shift):
    """
    O(r) space
    :param array:
    :param shift:
    :return:
    """
    n = len(array)
    shift = shift % n
    shift_arr = array[n - shift:]
    array[shift:] = array[:n - shift]
    array[:shift] = shift_arr


def rotate_array_in_place(array, k):
    n = len(array)
    reverse_array(array, 0, n - 1)
    reverse_array(array, 0, k - 1)
    reverse_array(array, k, n - 1)


def reverse_array(array, left, right):
    while left < right:
        array[left], array[right] = array[right], array[left]
        left += 1
        right -= 1


if __name__ == '__main__':
    array = [1, 2, 3, 4, 5]
    rotate_array_in_place(array, 2)
    print array
