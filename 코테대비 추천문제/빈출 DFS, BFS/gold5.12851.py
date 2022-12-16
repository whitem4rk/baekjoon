from collections import deque

a, b = map(int, input().split())
visited = [0] * 100001

way = 0
short = -1

q = deque([(a,0)])

while q:
    n, depth = q.popleft()
    visited[n] = True
    if n == b:
        if short == -1:
            short = depth
        
        if short == depth:
            way += 1
            continue
        else:
            break
            
    
    for x in [n-1,n+1,2*n]:
        if 0 <= x <= 100000:
            if not visited[x]:
                q.append((x,depth+1))
                
print(short, way)
