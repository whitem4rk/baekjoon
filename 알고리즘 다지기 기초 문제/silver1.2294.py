n, k = map(int, input().split())

coinlist = []
for _ in range(n):
    coinlist.append(int(input()))
coinlist.sort(reverse=True)

dplist = [10001 for _ in range(k+1)]
dplist[0] = 0

for coin in coinlist:
    for i in range(coin,k+1):
        print(dplist)
        dplist[i] = min(dplist[i],dplist[i-coin]+1)
if dplist[k] == 10001:
    print(-1)
else:
    print(dplist[k])