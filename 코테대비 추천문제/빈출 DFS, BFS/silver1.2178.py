from collections import deque

height, width = map(int, input().split())

graph = [list(map(int,input())) for i in range(height)]
visited = [[False]*width for i in range(height)]
dh = [0,0,1,-1]
dw = [1,-1,0,0]

def bfs():
    global height
    global width
    queue = deque([(0,0,1)])
    
    while queue:
        h, w, depth = queue.popleft()
        if h == height-1 and w == width-1:
            print(depth)
            exit()
        
        if not visited[h][w]:
            visited[h][w] = True
            for i in range(4):
                if 0 <= h+dh[i] and h+dh[i] <height and 0 <= w+dw[i] and w+dw[i] < width:
                    if graph[h+dh[i]][w+dw[i]] == 1:
                        queue.append((h+dh[i], w+dw[i], depth+1))
                    
bfs()