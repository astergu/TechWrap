class Solution(object):
    def subsets(self, nums):
        """
        :type nums: List[int]
        :rtype: List[List[int]]
        """
        def dfs(res, nums):
            ans.append(res)
            for i in xrange(len(nums)):
                dfs(res + [nums[i]], nums[i+1:])

        ans = []
        dfs([], nums)
        return ans


if __name__ == '__main__':
    nums = [1,2,3]
    s = Solution()
    ret = s.subsets(nums)
    print ret
