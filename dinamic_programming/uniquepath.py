def uniquePaths(m, n):
    dp = [[0] * n for i in range(m)]
    for i in range(n):
        dp[0][i] = 1
    for j in range(m):
        dp[j][0] = 1
    for i in range(1, m):
        for j in range(1, n):
            dp[i][j] = dp[i-1][j] + dp[i][j-1]
    for row in dp:
        print(row) 
    return dp[m-1][n-1]
print(uniquePaths(3, 7))