"""
Given a collection of candidate numbers (candidates) and a target number (target), find all unique combinations in candidates where the candidate numbers sums to target.

Each number in candidates may only be used once in the combination.

Note:

    All numbers (including target) will be positive integers.
    The solution set must not contain duplicate combinations.

Example 1:

Input: candidates = [10,1,2,7,6,1,5], target = 8,
A solution set is:
[
  [1, 7],
  [1, 2, 5],
  [2, 6],
  [1, 1, 6]
]

Example 2:

Input: candidates = [2,5,2,1,2], target = 5,
A solution set is:
[
  [1,2,2],
  [5]
]
"""


class Solution:
    def combinationSum2(self, candidates, target):
        ans = []
        N = len(candidates)

        def dfs(sum_, goal, curr, start):
            print("{}, {}, {}, {}, {}".format(sum_, goal, curr, start, ans))
            if goal == 0:
                ans.append(curr)
            elif target > 0:
                for i in range(start, N):
                    num = candidates[i]
                    dfs(sum_ + num, goal - num, curr + [num], i + 1)

        for i, element in enumerate(candidates):
            if element < target:
                dfs(element, target - element, [element], i + 1)

        ans = [(sorted(item), len(item)) for item in ans]
        ans = sorted(ans, key=lambda x: x)
        ret = []
        if ans:
            ret = [ans[0][0]]
        for i in range(1, len(ans)):
            if ans[i][0] != ans[i - 1][0]:
                ret.append(ans[i][0])

        return ret


if __name__ == '__main__':
    s = Solution()
    candidates = [2, 5, 2, 1, 2]
    target = 5
    print(s.combinationSum2(candidates, target))
