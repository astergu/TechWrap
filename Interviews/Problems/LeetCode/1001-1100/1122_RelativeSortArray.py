"""
Given two arrays arr1 and arr2, the elements of arr2 are distinct, and all elements in arr2 are also in arr1.

Sort the elements of arr1 such that the relative ordering of items in arr1 are the same as in arr2.  Elements that don't appear in arr2 should be placed at the end of arr1 in ascending order.



Example 1:

Input: arr1 = [2,3,1,3,2,4,6,7,9,2,19], arr2 = [2,1,4,3,9,6]
Output: [2,2,2,1,4,3,3,9,6,7,19]



Constraints:

    arr1.length, arr2.length <= 1000
    0 <= arr1[i], arr2[i] <= 1000
    Each arr2[i] is distinct.
    Each arr2[i] is in arr1.


"""

from collections import defaultdict


class Solution:
    def relativeSortArray(self, arr1, arr2):
        ret = []
        all_v = defaultdict(int)
        for i in arr1:
            all_v[i] += 1
        for j in arr2:
            if j in all_v:
                ret.extend([j] * all_v[j])

        unseen = [(k, v) for k, v in all_v.items() if k not in arr2]
        sort_unseen = sorted(unseen, key=lambda item: item[0])
        for item in sort_unseen:
            ret.extend([item[0]] * item[1])
        return ret

    def topSolution(self, arr1, arr2):
        dic = {arr2[i]: i for i in range(len(arr2))}
        arr1.sort(key=lambda x: (dic.get(x, 1001), x))
        return arr1


if __name__ == '__main__':
    s = Solution()
    arr1 = [2, 3, 1, 3, 2, 4, 6, 7, 9, 2, 19]
    arr2 = [2, 1, 4, 3, 9, 6]
    ret = s.relativeSortArray(arr1, arr2)
    print(ret)
