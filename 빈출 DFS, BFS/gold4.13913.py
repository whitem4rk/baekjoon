from collections import deque
import copy

a, b = map(int, input().split())
visitlist = [-1] * 100001
visited = [False] * 100001
short = -1

q = deque([(a,0)])
visitlist.append(a)
visited[a] = True

while q:
    cur, depth = q.popleft()

    if cur == b:
        print(depth)
        arr = []
        temp = cur
        for _ in range(depth+1):
            arr.append(temp)
            temp = visitlist[temp]
        arr.reverse()
        print(' '.join(map(str, arr)))
        
        break
        
    for x in [cur-1,cur+1,2*cur]:
        if 0 <= x <= 100000:
            if not visited[x]:
                q.append((x,depth+1))
                visited[x] = True
                visitlist[x] = cur
                visitlist.append(x)
                
