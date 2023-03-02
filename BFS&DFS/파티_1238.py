import sys
import heapq
input = sys.stdin.readline
INF = int(1e9)

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
ans =[]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))

def dijkstra(start,target):
    distance = [INF]*(n+1)
    q = []
    heapq.heappush(q,(0,start))
    distance[start]=0

    while q:
        dist,now = heapq.heappop(q)
        if distance[now]<dist:
            continue
        for i,j in graph[now]:
            cost = dist+j
            if distance[i]>cost:
                distance[i]=cost
                heapq.heappush(q,(cost,i))
    return distance[target]


for i in range(1,n+1):
    ans.append(dijkstra(i,x))
    ans[i-1]=ans[i-1]+dijkstra(x,i)

print(max(ans))



