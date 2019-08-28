"""
Given a set of candidate numbers (candidates) (without duplicates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

The same repeated number may be chosen from candidates unlimited number of times.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [2,3,6,7], target = 7,
A solution set is:
[
  [7],
  [2,2,3]
]

Example 2:

Input: candidates = [2,3,5], target = 8,
A solution set is:
[
  [2,2,2,2],
  [2,3,3],
  [3,5]
]


"""


class Solution:
    def combinationSum(self, candidates, target):
        ans = []
        N = len(candidates)

        def dfs(part, sum_, goal, index):
            if sum_ == target:
                ans.append(part)
            else:
                for i in range(N - index):
                    cur = candidates[index + i]
                    if cur <= goal:
                        dfs(part + [cur], sum_ + cur,
                            goal - cur, index + i)

        for i in range(N):
            mem = candidates[i]
            dfs([mem], mem, target - mem, i)

        return ans


if __name__ == '__main__':
    candidates = [2, 3, 6, 7]
    target = 7
    s = Solution()
    print(s.combinationSum(candidates, target))
