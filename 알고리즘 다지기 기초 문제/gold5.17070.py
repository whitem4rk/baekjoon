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