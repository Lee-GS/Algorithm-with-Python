import sys
import heapq

input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(e)]
INF = int(1e9)
distance = [INF]*(n+1)
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))
v1,v2 = map(int,input().split())

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start))
    distance[start] = 0

    while q:
        dist, now = heapq.heappop()
        if distance[now]<dist:
            continue
        for i,j in graph[now]:
            cost = dist+j
            if cost < distance[i]:
                distance[i]=cost
                if i == v1 or i ==v2:
                    heapq.heappush(q,(cost,i))



