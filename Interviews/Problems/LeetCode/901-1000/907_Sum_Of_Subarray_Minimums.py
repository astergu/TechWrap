"""
Given an array of integers A, find the sum of min(B), where B ranges over every (contiguous) subarray of A.

Since the answer may be large, return the answer modulo 10^9 + 7.



Example 1:

Input: [3,1,2,4]
Output: 17
Explanation: Subarrays are [3], [1], [2], [4], [3,1], [1,2], [2,4], [3,1,2], [1,2,4], [3,1,2,4].
Minimums are 3, 1, 2, 4, 1, 1, 2, 1, 1, 1.  Sum is 17.



Note:

    1 <= A.length <= 30000
    1 <= A[i] <= 30000

"""


class Solution:
    def sumSubarrayMins_1(self, A):  # Memory Limit Exceeded
        modulo = pow(10, 9) + 7

        def sub_cont_arr(A):
            ret = []
            for i in range(len(A)):
                for j in range(i + 1, len(A) + 1):
                    ret.append(A[i:j])
            return ret

        A_subarr = sub_cont_arr(A)
        sum_min = sum([min(sub) for sub in A_subarr if sub])
        return sum_min % modulo

    def sumSubarrayMins(self, A):
        if not A:
            return 0

        n = len(A)
        left, right = [None] * n, [None] * n
        s1, s2 = [], []
        cnt = 1
        for i in range(n):
            while len(s1) > 0 and s1[-1][0] > A[i]:
                cnt += s1[-1][1]
                s1.pop()
            s1.append([A[i], cnt])
            left[i] = cnt
        print(left)

        for i in range(n - 1, -1, -1):
            cnt = 1
            while len(s2) > 0 and s2[-1][0] > A[i]:
                cnt += s2[-1][1]
                s2.pop()
            s2.append([A[i], cnt])
            right[i] = cnt
        print(right)

        res = 0
        for i in range(n):
            res += A[i] * left[i] * right[i]
        return res


if __name__ == '__main__':
    s = Solution()
    A = [3, 1, 2, 4]
    print(s.sumSubarrayMins(A))
