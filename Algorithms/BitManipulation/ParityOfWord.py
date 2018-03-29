#!/usr/bin/env python


def parity_of_word(x):
    """
    Time Complexity: the number of bits to represent the number.
    :param x:
    :return:
    """
    res = 0
    while x:
        res ^= x & 1
        x >>= 1
    return res


def parity_of_word_improved(x):
    """
    Time complexity: O(k), k is the number of 1s in the number.
    :param x:
    :return:
    """
    res = 0
    while x:
        res ^= 1
        x &= x - 1 # Drops the lowest set bit of x.
    return res


def parity_split(x):
    """
    assume x is 64-bit number. Time complexity: O(logn), n is the word size.
    :param x:
    :return:
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


def parity_larger_number(x):
    """
    Time complexity: O(n/L), L is the length of the words for which we cache,
                        in this case, L is 16.
    :param x:
    :return:
    """
    precomputed_parity = {} # needs to be precomputed
    mask_size = 16
    bit_mask = 0xFFFF
    return (precomputed_parity[x >> (3 * mask_size)] ^ \
            precomputed_parity[x >> (2 * mask_size)] & bit_mask ^ \
            precomputed_parity[x >> mask_size] & bit_mask ^ \
            precomputed_parity[x & bit_mask])


if __name__ == '__main__':
    print parity_of_word_improved(12)