from collections import deque

vertex = int(input())
edge = int(input())
v_dict = {}

for i in range(vertex):
    v_dict[i+1] = set()

for i in range(edge):
    x ,y = map(int, input().split())
    v_dict[x].add(y)
    v_dict[y].add(x)
    

def bfs(dict):
    queue = deque([1])
    visited = []
    
    while queue:
        n = queue.popleft()
        if n not in visited:
            visited.append(n)
            queue += dict[n] - set(visited)
            
    print(len(visited)-1)
    return

bfs(v_dict)