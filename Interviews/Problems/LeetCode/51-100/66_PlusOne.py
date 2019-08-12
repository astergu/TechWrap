"""
Given a non-empty array of digits representing a non-negative integer, plus one to the integer.

The digits are stored such that the most significant digit is at the head of the list, and each element in the array contain a single digit.

You may assume the integer does not contain any leading zero, except the number 0 itself.

Example 1:

Input: [1,2,3]
Output: [1,2,4]
Explanation: The array represents the integer 123.

Example 2:

Input: [4,3,2,1]
Output: [4,3,2,2]
Explanation: The array represents the integer 4321.

"""


class Solution:
    def plusOne(self, digits):
        carry = 1
        plus_digits = []
        for d in digits[::-1]:
            x = d + carry
            carry, rem = int(x / 10), x % 10
            plus_digits.append(rem)
        if carry:
            plus_digits.append(carry)
        return plus_digits[::-1]

    def plusOne2(self, digits):
        if not digits:
            return [1]
        if digits[-1] < 9:
            digits[-1] += 1
        else:
            if len(digits) == 1:
                digits = [1, 0]
            else:
                digits = self.plusOne2(digits[:-1]) + [0]
        return digits


if __name__ == '__main__':
    s = Solution()
    print(s.plusOne2([4, 3, 2, 1]))
    print(s.plusOne2([9]))
