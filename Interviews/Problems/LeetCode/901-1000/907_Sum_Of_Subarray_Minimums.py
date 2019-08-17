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

        def subarr(A):
            ret = [[]]
            for item in A:
                tmp = []
                for x in ret:
                    tmp.append(x + [item])
                ret.extend(tmp)
            return ret

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
        pass


if __name__ == '__main__':
    s = Solution()
    A = [3, 1, 2, 4]
    # print(s.sumSubarrayMins_1(A))
    s.sumSubarrayMins_1(A)
