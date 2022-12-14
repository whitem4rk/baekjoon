from collections import deque

h, w, trash = map(int, input().split())
dh = [0,0,1,-1]
dw = [1,-1,0,0]

graph = [[0]*w for _ in range(h)]

for i in range(trash):
    y,x = map(int,input().split())
    graph[y-1][x-1] = 1

big = 0
def bfs(start_y, start_x):
    global big

    cnt = 0
    q = deque([(start_y,start_x)])
    
    while q:
        y,x = q.popleft()
        graph[y][x] = 0
        cnt += 1
        big = max(cnt,big)
        for i in range(4):
            if 0<=y+dh[i] and 0<=x+dw[i] and y+dh[i]<h and x+dw[i]<w:
                if graph[y+dh[i]][x+dw[i]] == 1:
                    q.append((y+dh[i],x+dw[i]))
                    graph[y+dh[i]][x+dw[i]] = 0
for i in range(h):
    for j in range(w):
        if graph[i][j] == 1:
            bfs(i,j)
print(big)