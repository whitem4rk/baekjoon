H, W = map(int, input().split())
ground = list(map(int, input().split()))

rain = 0
for i in range(H):
    gap = 0
    started = False
    for j in range(W):
        if ground[j] > i and started == False:
            started = True
            gap = 0
        elif ground[j] > i and started == True:
            rain += gap
            gap = 0
        elif ground[j] <= i and started == True:
            gap += 1
        else:
            continue
        
print(rain)