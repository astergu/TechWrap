#!/usr/bin/env python

"""
Implement a function rotateArray(vector<int> arr, int r) which rotates the array by r places.
Eg 1 2 3 4 5 on being rotated by 2 gives 4 5 1 2 3.

Naive implementation: use extra space O(n), time O(n).

Follow up:
    Could you do it in-place?
"""

# Solution 1
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

# Solution 2
def rotate_array_rec(array, k):
    shift(array, len(array), 0, k)


def shift(a, n, pos, step):
    prev = (pos - step) % n
    if prev == 0:
        x = a[0]
    else:
        x = shift(a, n, prev, step)
    y = a[pos]
    a[pos] = x
    return y


# Solution 3
def rotate_array_seq(array, k):
    n = len(array)
    k = k % n
    prev, prev_val = 0, array[0]
    for i in xrange(n):
        pos = (prev + k) % n
        tmp, prev = prev_val, pos
        prev_val = array[pos]
        array[pos] = tmp


# Solution 4
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
    rotate_array_seq(array, 2)
    print array
