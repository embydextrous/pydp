'''
Given a set of n elements, find number of ways of partitioning it.
Examples:

Input:  n = 2
Output: Number of ways = 2
Explanation: Let the set be {1, 2}
            { {1}, {2} } 
            { {1, 2} }

Input:  n = 3
Output: Number of ways = 5
Explanation: Let the set be {1, 2, 3}
             { {1}, {2}, {3} }
             { {1}, {2, 3} }
             { {2}, {1, 3} }
             { {3}, {1, 2} }
             { {1, 2, 3} }. 

Solution to above questions is Bell Number.

What is a Bell Number?
Let S(n, k) be total number of partitions of n elements into k sets. 
The value of n'th Bell Number is sum of S(n, k) for k = 1 to n.

Value of S(n, k) can be defined recursively as, S(n+1, k) = k*S(n, k) + S(n, k-1)

A Better Method is to use Bell Triangle. Below is a sample Bell Triangle for first few Bell Numbers.

1
1 2
2 3 5
5 7 10 15
15 20 27 37 52

The triangle is constructed using below formula.

// If this is first column of current row 'i'
If j == 0
   // Then copy last entry of previous row
   // Note that i'th row has i entries
   Bell(i, j) = Bell(i-1, i-1) 

// If this is not first column of current row
Else 
   // Then this element is sum of previous element 
   // in current row and the element just above the
   // previous element
   Bell(i, j) = Bell(i-1, j-1) + Bell(i, j-1)
'''

def bellNumber(n):
    bell = [[0 for i in range(n+1)] for j in range(n+1)]
    bell[0][0] = 1
    for i in range(1, n+1):
        for j in range(i+1):
            if j == 0:
                bell[i][j] = bell[i-1][i-1]
            else:
                bell[i][j] = bell[i][j-1] + bell[i-1][j-1]
    return bell[n][0]

n = 6
print bellNumber(n)