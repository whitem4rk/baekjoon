import heapq
import sys
input = sys.stdin.readline

city = int(input())
bus = int(input())
INF = sys.maxsize

distance = [INF] * (city+1)
citylist = [[] for _ in range(city+1)]

for i in range(bus):
    start, end, dist = map(int,input().split())
    citylist[start].append((end, dist))

def dijk(first, last):
    queue = []
    heapq.heappush(queue, (first, 0))
    distance[first] = 0
    
    while queue:
        cur, cur_dist = heapq.heappop(que   ue)
        if distance[cur] < cur_dist:
            continue
        for end, dist in citylist[cur]:
            if distance[end] > cur_dist + dist:
                distance[end] = cur_dist + dist
                heapq.heappush(queue, (end, distance[end]))
    print(distance[last])

start, end = map(int, input().split())
dijk(start,end)