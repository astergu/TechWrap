"""
Given a 2D board and a word, find if the word exists in the grid.

The word can be constructed from letters of sequentially adjacent cell, where "adjacent" cells are those horizontally or vertically neighboring. The same letter cell may not be used more than once.

Example:

board =
[
  ['A','B','C','E'],
  ['S','F','C','S'],
  ['A','D','E','E']
]

Given word = "ABCCED", return true.
Given word = "SEE", return true.
Given word = "ABCB", return false.
"""

class Solution(object):
    def exist(self, board, word):
        """
        :type board: List[List[str]]
        :type word: str
        :rtype: bool
        """
        if not board:
            return False
        for i in xrange(len(board)):
            for j in xrange(len(board[i])):
                if self.dfs(board, i, j, word):
                    return True
        return False

    def dfs(self, board, i, j, word):
        if len(word) == 0:
            return True
        if i < 0 or i >= len(board) or j < 0 or j >= len(board[i]) or word[0] != board[i][j]:
            return False
        tmp = board[i][j]
        print "tmp: ", tmp
        board[i][j] = '#' # avoid visit again
        res = self.dfs(board, i+1, j, word[1:]) or self.dfs(board, i-1, j, word[1:]) \
    or self.dfs(board, i, j+1, word[1:]) or self.dfs(board, i, j-1, word[1:])
        board[i][j] = tmp
        return res


if __name__ == '__main__':
    s = Solution()
    #board = [
    #      ['A','B','C','E'],
    #      ['S','F','C','S'],
    #      ['A','D','E','E']
    #        ]
    #word = "ABCCED"
    board = [["a"]]
    word = "b"
    print s.exist(board, word)
