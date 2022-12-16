width, height = map(int, input().split())
graph = [list(input()) for _ in range(height)]
visited = [[False] * width for _ in range(height)]

dx = [0, 0, 1, -1]
dy = [1, -1, 0, 0]

w_power = 0
b_power = 0

def dfs(y,x,flag):
    global count
    visited[y][x] = True
    count += 1
    for i in range(4):
        if y+dy[i] < height and 0 <= y+dy[i] and x+dx[i] < width and 0 <= x+dx[i]:
            if not visited[y+dy[i]][x+dx[i]] and graph[y+dy[i]][x+dx[i]] == flag:
                dfs(y+dy[i],x+dx[i],flag)

for i in range(height):
    for j in range(width):
        if visited[i][j]:
            continue
        
        if graph[i][j] == 'W':
            count = 0
            dfs(i,j,'W')
            w_power += count ** 2
        else:
            count = 0
            dfs(i,j,'B')
            b_power += count ** 2
            
print(w_power, b_power)