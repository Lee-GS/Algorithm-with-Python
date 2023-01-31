import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) #재귀제한을 늘려준다

N = int(input())

graph = [[]*(N+1) for _ in range(N+1)] # 그래프 생성
visited = [0]*(N+1)

for _ in range (N-1):
    a,b = map(int,input().split())
    graph[a].append(b) #쌍방향 연결이기 때문에
    graph[b].append(a) # 교차해서 넣어준다



def dfs(x):
    for i in graph[x]: #루트 노드인 1번 노드에 있는 값들부터 차례대로 넣어 재귀를 통해 값을 도출한다
        if visited[i] == 0: #미방문 했다면
            visited[i] = x #방문한 노드의 값을 넣어준다
            dfs(i) 
            
dfs(1)
for i in range(2,N+1): #2번노드 부터 보여줘야 하므로 2부터 시작
    print(visited[i])