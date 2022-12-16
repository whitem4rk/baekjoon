a,b = map(int, input().split())

ans = 1000000000
def dfs(start, depth):
    global ans
    if start > b:
        return
    elif start == b:
        ans = min(ans, depth)
    else:
        mul2 = start*2
        dfs(mul2, depth+1)
        
        plus1 = int(str(start)+str(1))
        dfs(plus1, depth+1)
        
dfs(a,1)
if ans == 1000000000:
    print(-1)
else:
    print(ans)