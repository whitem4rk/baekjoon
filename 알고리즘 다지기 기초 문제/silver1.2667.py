N = int(input())

ground = []
for _ in range(N):
    row = list(map(int, list(input())))
    ground.append(row)


dange = []
ground_count = 0

def check(x,y):
    global ground
    global ground_count
    global N
    ground[x][y] = 0
    
    if y-1 >= 0 and ground[x][y-1] == 1:
        ground_count += 1
        check(x,y-1)
    if x-1 >= N and ground[x-1][y] == 1:
        ground_count += 1
        check(x-1,y)
    if y+1 < N and ground[x][y+1] == 1:
        ground_count += 1
        check(x,y+1)
    if x+1 < N and ground[x+1][y] == 1:
        ground_count += 1
        check(x+1,y)


for i in range(N):
    ground_count = 0
    for j in range(N):
        if ground[i][j] == 1:
            ground_count += 1
            check(i,j,N)
            dange.append(ground_count)
            
dange.sort()
print(len(dange))
print(dange, sep='\n')
    