import sys
import heapq # 힙큐 
input = sys.stdin.readline
INF = int(1e9) # 무한

n = int(input())
m = int(input())
graph = [[] for _ in range(n+1)]
distance = [INF]*(n+1)

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # a 노드에서 b 노드로 갈때 c의 비용이 듬

x,y = map(int,input().split())

def dijkstra(start):
    q=[]
    heapq.heappush(q,(0,start)) #힙큐에 비용과 시작노드 삽입
    distance[start] = 0 # 시작 노드는 비용이 0이다
    
    while q:
        dist,now = heapq.heappop(q) # 순서대로 비용과 노드를 꺼낸다.
        if distance[now] < dist: # 꺼낸 노드의 비용이 먼저 기록되어 있던 노드의 비용보다 크다면 이미 최소 비용이 들어가 있는
                                 # 경우이기 때문에 작업을 수행할 필요가 없다.
            continue

        for i, j in graph[now]: # 노드가 가는 방향들을 반복해서 검사해준다
            cost = dist+j # 현재 노드의 비용과 앞으로 갈 방향의 노드의 비용들을 더해준다
            if cost<distance[i]: # 위에서 더한 비용의 값이 기존의 있던 비용의 값보다 작으면
                distance[i] = cost # 해당노드의 최소비용을 바꿔준다.
                heapq.heappush(q,(cost,i)) # 힙큐에 비용과 노드를 다시 삽입해 검사한다.

dijkstra(x)
print(distance[y])