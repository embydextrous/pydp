def permutationCoefficient(n, r):
    pc = [[0 for i in range(n + 1)] for j in range(n + 1)]
    pc[1][0] = 1
    pc[1][1] = 1
    for i in range(2, n + 1):
        for j in range(i + 1):
            if j == 0:
                pc[i][j] = 1
            else:
                pc[i][j] = pc[i-1][j] + j * pc[i-1][j-1]
    return pc[n][r]

def permutationCoefficientSpaceOptimized(n, r):
    pc = [[0 for i in range(n + 1)] for j in range(2)]
    pc[1][0] = 1
    pc[1][1] = 1
    for i in range(2, n + 1):
        pc[0] = pc[1][:]
        for j in range(i + 1):
            if j == 0:
                pc[1][j] = 1
            else:
                pc[1][j] = pc[0][j] + j * pc[0][j-1]
    return pc[1][r]

def permutationCoefficientSuperEfficient(n, r):
    result = 1
    for i in range(n - r + 1, n + 1):
        result *= i
    return result

print permutationCoefficient(7, 5)
print permutationCoefficientSpaceOptimized(7, 0)
print permutationCoefficientSuperEfficient(7, 1)