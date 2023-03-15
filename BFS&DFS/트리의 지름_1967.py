import heapq
import sys
input = sys.stdin.readline
INF = int(1e9)
n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
    graph[b].append((a,c))

def dijkstra(start):
    distance=[INF]*(n+1)
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i,j in graph[now]:
            cost = dist+j
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q,(cost,i))
    del distance[0]
    return max(distance)

_max=0

for i in range(1,n+1):
    tmp = dijkstra(i)
    if tmp > _max:
        _max = tmp
print(_max)





