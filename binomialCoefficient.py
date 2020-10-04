import time

def binomialCoefficient(n, r):
    bc = [[0 for i in range(n + 1)] for j in range(n + 1)]
    bc[1][0] = 1
    bc[1][1] = 1
    for i in range(2, n + 1):
        for j in range(i + 1):
            if j == 0:
                bc[i][j] = 1
            else:
                bc[i][j] = bc[i-1][j] + bc[i-1][j-1]
            if i == n and j == r:
                break
    return bc[n][r]

def binomialCoefficientSpaceOptimized(n, r):
    bc = [[0 for i in range(n+1)] for j in range(2)]
    bc[1][0] = 1
    bc[1][1] = 1
    for i in range(2, n+1):
        bc[0] = bc[1][:]
        for j in range(i+1):
            if j == 0:
                bc[1][j] = 1
            else:
                bc[1][j] = bc[0][j] + bc[0][j-1]
            if i == n and j == r:
                break
    return bc[1][r]

def binomialCoefficientSuperEfficient(n, r):
    r = min(r, n - r)
    result = 1
    for i in range(r):
        result *= (n - i)
        result /= (i + 1)
    return result

start = time.time() * 1000
print binomialCoefficient(1000, 375)
end = time.time() * 1000
print end - start

start = time.time() * 1000
print binomialCoefficientSpaceOptimized(1000, 375)
end = time.time() * 1000
print end - start

start = time.time() * 1000
print binomialCoefficientSuperEfficient(1000, 375)
end = time.time() * 1000
print end - start
