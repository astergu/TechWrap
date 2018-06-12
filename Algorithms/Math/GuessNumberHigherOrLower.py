class Solution(object):
    def guessNumber(self, n):
        """
        :type n: int
        :rtype: int
        """
        low, high = 1, n
        while low <= high:
            mid = (low + high) / 2
            ret = guess(mid)
            if ret == -1:
                high = mid - 1
            elif ret == 1:
                low = mid + 1
            else:
                return mid
        return -1
