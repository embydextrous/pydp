import time

# DP Based Algorithm - ~4500 times faster than recursive solution
def fibonacci(n):
    if n <= 1:
        return n
    a, b = 0, 1
    while n > 1:
        a, b = b, a + b
        n -= 1
    return b

def fib(n):
    if n <= 1:
        return n
    return fib(n - 1) + fib(n - 2)

# [0, 1, 1, 2, 3, 5, 8, 13, 21, 34, 55]
start = time.time() * 1000
print fibonacci(135000)
print time.time() * 1000 - start
start = time.time() * 1000
print fib(30)
print time.time() * 1000 - start