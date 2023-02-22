import heapq
import sys
input = sys.stdin.readline

v,e = map(int,input().split())
k = int(input())
graph = [[] for _ in range(v+1)]
INF = int(1e9)
distance = [INF]*(v+1)
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def djikstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now = heapq.heappop(q)
        
        if distance[now] < dist:
            continue
        for i,j in graph[now]:
            cost = dist+j
            if distance[i] > cost:
                distance[i] = cost
                heapq.heappush(q,(cost,i))
djikstra(k)

for i in range(1,len(distance)):
    if distance[i] == INF:
        print("INF")
    else:
        print(distance[i])