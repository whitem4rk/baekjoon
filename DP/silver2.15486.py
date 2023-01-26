import sys
input=sys.stdin.readline

n = int(input())
table = [list(map(int, input().split())) for _ in range(n)]
sum = [0] * (n+1)

cur = 0

for i in range(n):
    day = table[i][0]
    money = table[i][1]
    
    cur = max(cur, sum[i])
    
    if i+day <= n:
        sum[i+day] = max(sum[i+day], money+cur)

print(max(sum))
