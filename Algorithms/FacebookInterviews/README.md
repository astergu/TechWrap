Facebook面试准备的试题。

## Glassdoor Software Engineer Questions
- [x] [Write oode to raise a number to a power.](RaiseNumberToPower.py)
- [x] Suppose you have a matrix of numbers. How can you easily compute the [sum of any rectangle](SumOfRectangle.py) (i.e. a range \[row_start, row_end, col_start, col_end\]) of these numbers? How would you code this? 
    - Analysis: frequent queries on a static matrix, use dynamic programming
    - wiki: [https://en.wikipedia.org/wiki/Summed_area_table](https://en.wikipedia.org/wiki/Summed_area_table)
- [] You have two lightbulbs and a 100-storey building. You want to find the floor at which the bulbs will break when dropped. Find the floor using the least number of drops.
    - same idea as Google egg-dropping problem.
    - **first intuition**: use binary search. Start with floor 50, if the lightbulb breaks, then starts from 1 to 49. But if the lightbulb does not break, then drop it from 75, if it breaks, then try from 51 to 74. However, if in the first case, floor 49 is the answer, then you need to try 50 times, which is not a good solution.
    - **dynamic programming**: f(n) = min(1 + max(i - 1, f(n-i)))
- [] Implement a function [rotateArray(vector<int> arr, int r)](RotateArray.py) which rotates the array by r places. E.g. 1 2 3 4 5 on being rotated by 2 gives 4 5 1 2 3.
    - leetcode page: [Rotating array in place](https://articles.leetcode.com/rotating-array-in-place/) 

## Geeks For Geeks Software Engineer Questions
- [x] [Rotate and Delete](../Array/RotateAndDelete.py): Given an array of numbers (e.g. integers), there are two kinds of operations: rotate (clock-wise) and delete. 
Rotate the array *n* times and then delete the *n*th last element. If the *n*th last element does not exist then
deletes the first element present in the array. Your task is to find out which is the last
element that you deletes from the array so that the array becomes empty after removing it.
    - source: [https://practice.geeksforgeeks.org/problems/rotate-and-delete/0] (https://practice.geeksforgeeks.org/problems/rotate-and-delete/0)     
     
## Data Scientist Questions
- [] You're about to get on a plane to Seattle. You want to know if you should bring an umbrella. You call 3 random friends of yours who live there and ask each independently if it's raining. Each of your friends has a 2/3 chance of telling you the truth and a 1/3 chance of messing with you by lying. All 3 friends tell you that 
"Yes" it is raining. What is the probability that it's actually raining in Seattle?
