'''
Ugly numbers are numbers whose only prime factors are 2, 3 or 5. 
The sequence 1, 2, 3, 4, 5, 6, 8, 9, 10, 12, 15shows the first 11 ugly numbers. 
By convention, 1 is included.

Given a number n, the task is to find n'th Ugly number.

Examples:

Input  : n = 7
Output : 8

Input  : n = 10
Output : 12

Input  : n = 15
Output : 24

Input  : n = 150
Output : 5832
'''
def uglyNumber(n):
    ugly = [0] * n
    ugly[0] = 1
    i2 = i3 = i5 = 0
    nextMultipleOf2 = 2
    nextMultipleOf3 = 3
    nextMultipleOf5 = 5
    for i in range(1, n):
        ugly[i] = min(nextMultipleOf2, nextMultipleOf3, nextMultipleOf5)
        if ugly[i] == nextMultipleOf2:
            i2 += 1
            nextMultipleOf2 = ugly[i2] * 2
        if ugly[i] == nextMultipleOf3:
            i3 += 1
            nextMultipleOf3 = ugly[i3] * 3
        if ugly[i] == nextMultipleOf5:
            i5 += 1
            nextMultipleOf5 = ugly[i5] * 5
    return ugly[n-1]

print uglyNumber(150)
