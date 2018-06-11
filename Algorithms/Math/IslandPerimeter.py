#coding=utf8

class Solution(object):
    def islandPerimeter(self, grid):
        """
        :type grid: List[List[int]]
        :rtype: int
        """
        islands, neighbors = 0, 0
        for i in xrange(len(grid)):
            for j in xrange(len(grid[i])):
                if grid[i][j] == 1:
                    islands += 1
                    if i < len(grid) - 1 and grid[i + 1][j] == 1:
                        neighbors += 1
                    if j < len(grid[i]) - 1 and grid[i][j + 1] == 1:
                        neighbors += 1

        return islands * 4 - neighbors * 2


if __name__ == '__main__':
    grid = [[1, 1], [1, 1]]
    #grid = [[0,1,0,0],
    #     [1,1,1,0],
    #     [0,1,0,0],
    #     [1,1,0,0]]
    s = Solution()
    ret = s.islandPerimeter(grid)
    print ret
