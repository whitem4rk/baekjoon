from collections import deque

N, M, V = map(int, input().split())

graph = [[False] * (N + 1) for _ in range(N + 1)]

for _ in range(M):
    a, b = map(int, input().split())
    graph[a][b] = True
    graph[b][a] = True

visited_dfs = [False] * (N + 1) 
visited_bfs = [False] * (N + 1) 

bfslist = []
def bfs(V):
    q = deque([V]) 
    visited_bfs[V] = True
    while q:
        V = q.popleft() 
        bfslist.append(V)
        for i in range(1, N + 1): 
            if not visited_bfs[i] and graph[V][i]:  
                q.append(i) 
                visited_bfs[i] = True  


dfslist = []
def dfs(V):
    visited_dfs[V] = True 
    dfslist.append(V)
    for i in range(1, N + 1):
        if not visited_dfs[i] and graph[V][i]:  
            dfs(i) 

dfs(V)
bfs(V)
print(' '.join(map(str,dfslist)))
print(' '.join(map(str,bfslist)))