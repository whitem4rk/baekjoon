# 중복순열 - 시간초과
'''
from itertools import combinations_with_replacement

n, k = map(int, input().split())

coinlist = []
for _ in range(n):
    coinlist.append(int(input()))

coinlist.sort()

max_count = (k // coinlist[0]) +1
min_count = (k //coinlist[-1])
answer = 0

for i in range(min_count, max_count+1):
    for case in combinations_with_replacement(coinlist, i):
        if sum(case) == k:
            answer += 1
print(answer)
'''

# DFS - 반복문 초과
'''
n, k = map(int, input().split())

coinlist = []
for _ in range(n):
    coinlist.append(int(input()))
coinlist.sort()
goodcase = 0

def dfs(recent, dfssum):
    global goodcase
    print(f'{recent} , {dfssum}')
    if k == dfssum:
        goodcase += 1
        return
    elif dfssum > k:
        return
    
    for i in range(len(coinlist)):
        if recent <= coinlist[i]:
            dfs(coinlist[i],dfssum+coinlist[i])
                
dfs(coinlist[0],0)
print(goodcase)
'''


# DP
n, k = map(int, input().split())

dplist = [0 for _ in range(k+1)]
dplist[0] = 1

coinlist = []
for _ in range(n):
    coinlist.append(int(input()))
coinlist.sort()


for coin in coinlist:
    for i in range(coin,k+1):
        dplist[i] += dplist[i-coin]

print(dplist[k])