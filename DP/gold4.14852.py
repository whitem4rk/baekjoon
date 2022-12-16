x = int(input())
dp = [0]*1000001
dp[1] = 2
dp[2] = 7

sum = 0
for i in range(3,x+1):
    sum += (dp[i-3])%1000000007
    dp[i] = (dp[i-1]*2 + dp[i-2]*3 + sum*2 + 2)%1000000007

print(dp[x])