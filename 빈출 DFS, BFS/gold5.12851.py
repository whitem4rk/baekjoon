from collections import deque

a, b = map(int, input().split())

visited = [0] * 100001
way_cnt = 0
way = 0

q = deque([a])

while q:
    n = q.popleft()
    cnt = visited[n]
    
    if n == b:
        way_cnt = cnt
        way += 1
        continue
    
    for x in [n-1,n+1,2*n]:
        if 0 <= x <= 100000:
            if visited[x] == 0 or visited[x] == visited[n] + 1:
                q.append(x)
                visited[x] = cnt + 1
                
print(way_cnt, way)
