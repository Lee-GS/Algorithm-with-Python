import sys
sys.setrecursionlimit(10**9) # 이문제에선 해주지 않았더니 recursionerror가 떴다.
input = sys.stdin.readline

n = int(input())
graph = [[] for _ in range(n+1)]
for _ in range(n-1):
    a,b,c = map(int,input().split())
    graph[a].append((b,c))# 무방향 그래프이므로
    graph[b].append((a,c))# 두 노드 모두에 추가시켜준다.

distance = [-1]*(n+1) #거리를 나타낼 리스트이다.

def dfs(start,cost):
    for i,j in graph[start]: # 해당 노드의 요소를 뺀다
        a,b = i,j # 각각 a,b에 매칭시킨다
        if distance[a] == -1: # 방문하지 않았을경우
            distance[a] = b + cost # 해당 노드의 거리값과 출발한 노드의 간선의 값을 합해서 넣어준다
            dfs(a, b+cost) # 재귀를 해준다

distance[1] = 0 # 1번 노드부터 탐색해준다 
dfs(1,0)

node = distance.index(max(distance))# 첫번째 탐색이 끝나고 가장 멀리있는 노드를 찾아준다.
distance = [-1]*(n+1)
distance[node] = 0 # 가장 멀리있는 노드에서부터 다시 탐색한다
dfs(node,0)

print(max(distance)) # 최댓값 출력!!

