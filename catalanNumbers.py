'''
Catalan numbers satisfy the following recursive formula. 
 

C(0) = 1 
C(n+1) = summation(C(i)C(n-i)) for i in [0, n]
Following is the implementation of above recursive formula. 
'''

def catalanNumber(n):
    catalan = [0] * n
    catalan[0] = 1
    for i in range(1, n):
        for j in range(i):
            catalan[i] += catalan[i-j-1] * catalan[j]
    return catalan[n-1]

n = 10
print catalanNumber(n)