# #top down
def fabi(n, memo={}):
    if n in memo:
        return memo[n]
    if n <= 1:
        return n
    memo[n] = fabi(n-1, memo) + fabi(n-2, memo)
    return memo[n]
memo={}
print(fabi(5, memo))

# bottom up
# def fabi(n):
#     if n <= 1:
#         return n    
#     dp = [0] * (n + 1)
#     dp[0] = 1
#     dp[1] = 2
#     for i in range(2, n + 1):
#         dp[i] = dp[i - 1] + dp[i - 2]
#     return dp[n]
# print(fabi(7))
