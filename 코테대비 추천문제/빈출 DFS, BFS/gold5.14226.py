from collections import deque

s = int(input())
visited = [False] * 1001
queue = deque([(1, 0, 0)])

while queue:
    cur, depth, clip = queue.popleft()
    visited[cur] = True
    #print(f'visited {cur} | depth {depth} | clip {clip}')
    if cur == s:
        print(depth)
        break
    
    
    if  1 <= cur+clip <= 1000 and not visited[cur+clip]:
        queue.append((cur+clip,depth+1,clip))
    if  1 <= cur-1 <= 1000 and not visited[cur-1]:
        queue.append((cur-1, depth+1,clip))
    if clip != cur:
        queue.append((cur,depth+1,cur))