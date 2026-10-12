def min_path(nums):
    m, n = len(nums), len(nums[0])
    dp = [[0] * n for i in range(m)]
    
    for i in range(m):
        for j in range(n):
            if i == 0 and j == 0:
                dp[i][j] = nums[i][j]
            elif i == 0:
                dp[i][j] = dp[i][j-1] + nums[i][j]
            elif j == 0:
                dp[i][j] = dp[i-1][j] + nums[i][j]
            else:
                dp[i][j] = min(dp[i-1][j], dp[i][j-1]) + nums[i][j]
    
    return dp[m-1][n-1]
print(min_path([[1,3,1],[1,5,1],[4,2,1]]))
             
