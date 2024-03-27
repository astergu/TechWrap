'''
Anti-theft security devices are activated inside a bank. You are given a 0-indexed binary string array bank representing the floor plan of the bank, which is an m x n 2D matrix. bank[i] represents the ith row, consisting of '0's and '1's. '0' means the cell is empty, while'1' means the cell has a security device.

There is one laser beam between any two security devices if both conditions are met:

The two devices are located on two different rows: r1 and r2, where r1 < r2.
For each row i where r1 < i < r2, there are no security devices in the ith row.
Laser beams are independent, i.e., one beam does not interfere nor join with another.

Return the total number of laser beams in the bank.
'''

from typing import List

class Solution:
    def numberOfBeams(self, bank: List[str]) -> int:
        prev = None
        sum_beams = 0
        for b in bank:
            cnt = b.count('1')
            print("[count] {}".format(cnt))
            if cnt == 0:
                continue
            if prev is not None:
                sum_beams += prev * cnt
            print("[number_of_beams] ", sum_beams)
            prev = cnt
        
        return sum_beams


if __name__ == '__main__':
    sol = Solution()
    #bank = ["011001","000000","010100","001000"]
    bank = ["000","111","000"]
    print(sol.numberOfBeams(bank))