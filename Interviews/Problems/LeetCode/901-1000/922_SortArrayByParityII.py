"""
Given an array A of non-negative integers, half of the integers in A are odd, and half of the integers are even.

Sort the array so that whenever A[i] is odd, i is odd; and whenever A[i] is even, i is even.

You may return any answer array that satisfies this condition.



Example 1:

Input: [4,2,5,7]
Output: [4,5,2,7]
Explanation: [4,7,2,5], [2,5,4,7], [2,7,4,5] would also have been accepted.



Note:

    2 <= A.length <= 20000
    A.length % 2 == 0
    0 <= A[i] <= 1000

"""


class Solution:
    def sortArrayByParityII(self, A):
        keys = []
        for i in range(len(A)):
            if abs(A[i] - i) % 2 == 0:
                continue
            if keys:
                if abs(A[keys[0]] - A[i]) % 2 != 0:
                    key = keys.pop()
                    temp = A[key]
                    A[key] = A[i]
                    A[i] = temp
                else:
                    keys.append(i)
            else:
                keys.append(i)
        return A

    def topSolution(self, A):
        j = 1
        for i in range(0, len(A), 2):
            if A[i] % 2:
                while A[j] % 2:
                    j += 2
                A[i], A[j] = A[j], A[i]
        return A


if __name__ == '__main__':
    s = Solution()
    #A = [4, 2, 5, 7]
    A = [648, 831, 560, 986, 192, 424, 997, 829, 897, 843]
    print(s.sortArrayByParityII(A))
