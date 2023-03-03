import sys
import heapq
input = sys.stdin.readline
INF = int(1e9) # 무한 선언

n,m,x = map(int,input().split())
graph = [[] for _ in range(n+1)]
ans =[]

for _ in range(m):
    a,b,c = map(int,input().split())
    graph[a].append((b,c)) # a노드에서 b 노드로 가는 c의 거리가 든다.

def dijkstra(start,target):
    distance = [INF]*(n+1) #각 마을별로 갈 최소거리를 담을 리스트 선언
    q = []
    heapq.heappush(q,(0,start)) # 힙큐 선언
    distance[start]=0 # 현재 시작 지점은 0이다.

    while q:
        dist,now = heapq.heappop(q) #순서대로 거리와 위치이다
        if distance[now]<dist:
            continue
        for i,j in graph[now]:
            cost = dist+j
            if distance[i]>cost:
                distance[i]=cost
                heapq.heappush(q,(cost,i))
    return distance[target] # 도착지점의 거리값을 리턴한다.

# 이 부분이 문제에서 추가된 조건이다
# 오고 가는데 걸리는 시간이므로 왔다 갔다 즉 2번 구해야한다.
for i in range(1,n+1): 
    ans.append(dijkstra(i,x))# 오고
    ans[i-1]=ans[i-1]+dijkstra(x,i) # 가는거

#각 마을에서 2번마을로 가는거
#[4,0,6,3]
#2번 마을에서 각 마을로 가는거
#[1,0,3,7]
#위의 값들을 더하면 [5,0,9,10]이므로 답은 10이 나오게 된다

print(max(ans))



