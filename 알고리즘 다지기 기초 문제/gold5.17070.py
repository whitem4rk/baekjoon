# DFS - TIME LIMIT
'''
width = int(input())
miro = []

for i in range(width):
    miro.append(list(map(int,input().split())))

def dfs(row,col,state):
    global answer
    if row == width-1 and col == width-1:
        answer += 1
        return
    
    if state == 0 or state == 1:
        if col < width-1 and miro[row][col+1] == 0:
            dfs(row,col+1,0)
    if state == 1 or state == 2:
        if row < width-1 and miro[row+1][col] == 0:
            dfs(row+1,col,2)
    if state == 0 or state == 1 or state == 2:
        if col < width-1 and row < width-1 and miro[row][col+1] == 0 and miro[row+1][col] == 0 and miro[row+1][col+1] == 0:
            dfs(row+1,col+1,1)
    
answer = 0
dfs(0,1,0)
print(answer)
'''

# DP

width = int(input())
graph = [list(map(int, input().split())) for _ in range(width)]
dp = [[[0] * width for _ in range(width)] for _ in range(3)]
dp[0][0][1] = 1

for i in range(0, width):
    for j in range(1, width):
        
        if i == 0 and j == 1:
            continue
        
        if graph[i][j] == 0 and graph[i - 1][j] == 0 and graph[i][j - 1] == 0:
            dp[2][i][j] = sum(dp[k][i - 1][j - 1] for k in range(3))
        
        if graph[i][j] == 0:
            dp[0][i][j] = dp[0][i][j - 1] + dp[2][i][j - 1]
            dp[1][i][j] = dp[1][i - 1][j] + dp[2][i - 1][j]
        
print(sum(dp[k][-1][-1] for k in range(3)))