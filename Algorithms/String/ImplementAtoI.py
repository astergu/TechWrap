"""
Implement atoi to convert a string to an integer.

Hint: Carefully consider all possible input cases. If you want a challenge, please do not see below and ask yourself what are the possible input cases.

Notes: It is intended for this problem to be specified vaguely (ie, no given input specs). You are responsible to gather all the input requirements up front.
"""


def myAtoi(self, str):
    """
    :type str: str
    :rtype: int
    """
    if len(str) == 0:
        return 0
    ls = list(str.strip())

    sign = -1 if ls[0] == '-' else 1
    if ls[0] in ['-', '+']:
        del ls[0]
    ret, i = 0, 0
    while i < len(ls) and ls[i].isdigit():
        ret = ret * 10 + ord(ls[i]) - ord('0')
        i += 1
    return max(-2 ** 31, min(sign * ret, 2 ** 31 - 1))