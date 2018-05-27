/**
 * You are given a grid of cells with size N rows by M columns. A robot is situated at the bottom-left cell (row N-1, column 0). It can move from cell to cell but only to the right and to the top. Some cells are empty and the robot can pass through them but others are not and the robot cannot enter such cells. The robot cannot go outside the grid boundaries.

The robot has a goal to reach top-right cell (row 0, column M-1). Both the start and end cells are always empty. You need to compute the number of different paths that the robot can take from start to end. Only count paths that visit empty cells and move only to the right and up.

N and M will be numbers in the range [1, 512].

Write a method, which accepts the grid as an argument and returns one integer - the total number of different paths that the robot can take from the start to the end cell, MODULO 1,000,003. The reason we will use the modulo operation here is that the actual result could become a really big number and we don't want to let handling big numbers complicate the task more.

The input grid will contain N strings with M characters each - either '0' or '1', with '0' meaning an empty cell and '1' meaning an occupied cell. Each of these strings corresponds to a row in the grid.

 *
 *
 */



