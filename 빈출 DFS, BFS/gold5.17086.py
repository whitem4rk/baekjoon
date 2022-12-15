from collections import deque

h, w = map(int, input().split())
graph = [list(map(int, input().split())) for _ in range(h)]

dw = [1,1,1,0,-1,-1,-1,0]
dh = [1,0,-1,-1,-1,0,1,1]

q = deque()
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            q.append((i,j))
            
            

while q:
    curh,curw = q.popleft()
    for i in range(8):
        nw = curw + dw[i]
        nh = curh + dh[i]
        if 0 <= nw < w and 0 <= nh < h:
            if graph[nh][nw] == 0:
                q.append((nh,nw))
                graph[nh][nw] = graph[curh][curw] + 1

ans = 0
for i in range(h):
    for j in range(w):
        ans = max(graph[i][j], ans)
print(ans-1)