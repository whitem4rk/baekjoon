from collections import deque

h, w, maxMove = map(int, input().split())
graph = [list(input()) for _ in range(h)]
visited = [[-1 for _ in range(w)] for __ in range(h)]
x1, y1, x2,  y2 = map(int,input().split())

dh = [1,-1,0,0]
dw = [0,0,1,-1]

q = deque([(x1-1,y1-1)])
visited[x1-1][y1-1] = 0
short = -1

while q:
    curh, curw = q.popleft()
    # for i in range(h):
    #     print(visited[i])
    # print('----------------------')
    
    if curh == x2-1 and curw == y2-1:
        short = visited[curh][curw]
        break
    
    for i in range(4):
        for j in range(1, maxMove+1):
            nh = curh + dh[i]*j
            nw = curw + dw[i]*j 

            if not (0<=nh<h and 0<=nw<w) or graph[nh][nw] == '#':
                break
            if visited[nh][nw] != -1 and visited[nh][nw] <= visited[curh][curw]:
                break
            
            if visited[nh][nw] == -1:
                q.append((nh,nw))
                visited[nh][nw] = visited[curh][curw] + 1
            
print(short)

