import sys
import heapq

input = sys.stdin.readline

n,e = map(int,input().split())
graph = [[] for _ in range(n+1)]
INF = int(1e9) # 무한
for _ in range(e):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) #양방향 연결이므로
    graph[b].append((a,c)) #서로 엇갈리게 연결해준다


v1,v2 = map(int,input().split())

def dijkstra(start):
    distance = [INF]*(n+1) # 무한대의 노드별 거리를 선언해준다
    q=[] 
    heapq.heappush(q,(0,start)) # 힙큐에 삽압힌다
    distance[start] = 0 # 시작 노드는 거리를 0으로 해준다

    while q:
        dist,now = heapq.heappop(q) #순서대로 거리와 현재 노드의 위치이다
        if distance[now]<dist: # 현재 노드의 거리가 바뀐 위치의 거리보다 짧은경우 continue 해준다
            continue
        for i,j in graph[now]:
            cost = dist+j # 현재 노드의 거리와 앞으로 갈 노드의 거리의 합을 구해준다.
            if cost < distance[i]: # 위에서 더한 노드의 거리가 앞으로 갈 노드의 거리보다 작다면
                distance[i]=cost # 그 노드의 거리를 cost로 바꿔준다
                heapq.heappush(q,(cost,i)) # 그리고 힙큐에 삽입!
    return distance


first_way = dijkstra(1) # 출발점이 1일경우
second_way = dijkstra(v1) # 출발점이 v1일경우
third_way = dijkstra(v2) # 출발점이 v2일경우

v1_path = first_way[v1]+second_way[v2]+third_way[n] # 1 -> v1 -> v2 -> n
v2_path = first_way[v2]+third_way[v1]+second_way[n] # 1 -> v2 -> v1 -> n

total = min(v1_path,v2_path) #위에서 구한 경우중 더 거리가 짧은 경우를 구한다

print(total if total<INF else -1 ) # 출력조건에 맞게 출력!!
