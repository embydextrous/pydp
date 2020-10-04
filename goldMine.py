'''
Given a gold mine of n*m dimensions. Each field in this mine contains a positive integer which is 
the amount of gold in tons. Initially the miner is at first column but can be at any row. 
He can move only (right, right up, right down) that is from a given cell, the miner can move to the 
cell diagonally up towards the right or right or diagonally down towards the right. 
Find out maximum amount of gold he can collect.

Examples:

Input : mat[][] = {{1, 3, 3},
                   {2, 1, 4},
                  {0, 6, 4}};
Output : 12 
{(1,0)->(2,1)->(2,2)}

Input: mat[][] = { {1, 3, 1, 5},
                   {2, 2, 4, 1},
                   {5, 0, 2, 3},
                   {0, 6, 1, 2}};
Output : 16
(2,0) -> (1,1) -> (1,2) -> (0,3) OR
(2,0) -> (3,1) -> (2,2) -> (2,3)

Input : mat[][] = {{10, 33, 13, 15},
                  {22, 21, 04, 1},
                  {5, 0, 2, 3},
                  {0, 6, 14, 2}};
Output : 83
'''

def goldMine(mine):
    result = [row[:] for row in mine]
    R, C = len(result), len(result[0])
    maxSoFar = -1
    for i in range(1, C):
        for j in range(R):
            if j == 0 and j == R - 1:
                result[j][i] += result[j][i-1]
            elif j == 0:
                result[j][i] += max(result[j][i-1], result[j+1][i-1])
            elif j == R - 1:
                result[j][i] += max(result[j][i-1], result[j-1][i-1])
            else:
                result[j][i] += max(result[j][i-1], result[j+1][i-1], result[j-1][i-1])
            if i == C - 1:
                if result[j][i] > maxSoFar:
                    maxSoFar = result[j][i]
    return maxSoFar


mine = [[1, 3, 1, 5], [2, 2, 4, 1], [5, 0, 2, 3], [0, 6, 1, 2]]
print goldMine(mine)