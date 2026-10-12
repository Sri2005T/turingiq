def coinChange(coins, amount):
    n = len(coins)
    INF = float('inf')
    dp = [ [INF] * (amount+1) for i in range(n+1)]      
    for i in range(n+1):
        dp[i][0] = 0
    for i in range(1,n+1):
        for j in range(1,amount+1):
            coin = coins[i-1]
            exclude = dp[i-1][j]
            include = INF
            if coin <= j:
                include = 1 + dp[i][j-coin]
            dp[i][j] = min(include, exclude)
    if dp[n][amount] == float('inf'):
        return -1
    return dp[n][amount]
print(coinChange([1, 2, 5], 11))
# def coinChange(self, coins, amount):
#     INF = int(INF)
#     dp = [[-1]*(amount+1) for _ in range(len(coins))]
#     def helper(ind,target):
#         if target == 0:
#             return 0
#         if ind == len(coins):
#             if target  == 0:
#                 return 0
#             return INF
#         if dp[ind][target] == -1:
#             return dp[ind][target]
#         pick = INF
#         if coins[ind]<= target:
#             pick = 1+ helper(ind,target-coins[ind])
#         notPick = 0 + helper(ind+1,target)
#         dp[ind][target] =  min(pick,notPick)
#         return dp[ind][target]
#     value= helper(0,amount)
#     print(value)
#     if value == INF:
#         return -1
#     return value
# print(coinChange(None, [1, 2, 5], 11))
