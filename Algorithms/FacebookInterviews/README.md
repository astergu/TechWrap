Facebook面试准备的试题。

- [x] [Write oode to raise a number to a power.](RaiseNumberToPower.py)
- [x] Suppose you have a matrix of numbers. How can you easily compute the [sum of any rectangle](SumOfRectangle.py) (i.e. a range \[row_start, row_end, col_start, col_end\]) of these numbers? How would you code this? 
    - Analysis: frequent queries on a static matrix, use dynamic programming
    - wiki: [https://en.wikipedia.org/wiki/Summed_area_table](https://en.wikipedia.org/wiki/Summed_area_table)
- [] You have two lightbulbs and a 100-storey building. You want to find the floor at which the bulbs will break when dropped. Find the floor using the least number of drops.
    - same idea as Google egg-dropping problem.
    - **first intuition**: use binary search. Start with floor 50, if the lightbulb breaks, then starts from 1 to 49. But if the lightbulb does not break, then drop it from 75, if it breaks, then try from 51 to 74. However, if in the first case, floor 49 is the answer, then you need to try 50 times, which is not a good solution.
    - **dynamic programming**: f(n) = min(1 + max(i - 1, f(n-i)))