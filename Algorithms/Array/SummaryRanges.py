"""
Given a sorted integer array without duplicates, return the summary of its ranges.

Example 1:

Input:  [0,1,2,4,5,7]
Output: ["0->2","4->5","7"]
Explanation: 0,1,2 form a continuous range; 4,5 form a continuous range.
Example 2:

Input:  [0,2,3,4,6,8,9]
Output: ["0","2->4","6","8->9"]
Explanation: 2,3,4 form a continuous range; 8,9 form a continuous range.
"""


class Solution(object):
    def summaryRanges(self, nums):
        """
        :type nums: List[int]
        :rtype: List[str]
        """
        if not nums:
            return []
        last_start, last_num = None, None
        ans = []
        for num in nums:
            if last_start is None:
                last_start = num
            elif num - last_num > 1:
                if last_start == last_num:
                    ans.append(str(last_num))
                else:
                    crange = str(last_start) + "->" + str(last_num)
                    ans.append(crange)
                last_start = num
            last_num = num

        if last_start == last_num:
            ans.append(str(last_num))
        else:
            ans.append(str(last_start) + "->" + str(last_num))

        return ans


if __name__ == '__main__':
    input = [0,2,3,4,6,8,9]
    s = Solution()
    output = s.summaryRanges(input)
    print output
