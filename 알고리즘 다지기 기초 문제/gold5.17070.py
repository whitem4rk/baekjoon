width = int(input())
miro = []

for i in range(width):
    miro.append(list(map(int,input().split())))

answer = 0
def dfs(x,y,state):
    global answer
    if x >= width-1 and state == 0:
        return
    if y >= width-1 and state == 2:
        return
    elif miro[x][y] == 1:
        return
    elif x == width-1 and y == width-1:
        answer += 1
    
    if state == 0:
        if miro[x+1][y] == 0:
            dfs(x+1,y,0)
        if miro[x+1][y] == 0 and miro[x+1][y+1] == 0 and miro[x][y+1] == 0:
            dfs(x+1,y+1,1)
    elif state == 1:
        if miro[x+1][y] == 0:
            dfs(x+1,y,0)
        if miro[x+1][y] == 0 and miro[x+1][y+1] == 0 and miro[x][y+1] == 0:
            dfs(x+1,y+1,1)
        if miro[x][y+1] == 0:
            dfs(x,y+1,2)
    elif state == 2:
        if miro[x+1][y] == 0 and miro[x+1][y+1] == 0 and miro[x][y+1] == 0:
            dfs(x+1,y+1,1)
        if miro[x][y+1] == 0:
            dfs(x,y+1,2)
        
dfs(1,0,0)

print(answer)