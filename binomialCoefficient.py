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
    for row in bc:
        print row
    return bc[n][r]

print binomialCoefficient(24, 7)