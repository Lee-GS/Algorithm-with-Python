import sys
sys.setrecursionlimit(10**9) 

input = sys.stdin.readline

N = int(input())
a,b = map(int,input().split())
M = int(input())

graph=[[0]*(N+1) for _ in range(N+1)]
visited = [0]*(N+1)

for _ in range(M):
    x,y = map(int,input().split())
    graph[x].append(y) # 서로 이어져 있는 노드이니
    graph[y].append(x) # 서로 추가해준다.

def dfs(a):
    for i in graph[a]: # a번째 그래프에 들어있는 노드들의 차례대로 탐색해간다
        if(visited[i] == 0): # 미방문했다면 
            visited[i]=visited[a]+1 # a노드에 +1을 해주며 이어진 간선의 갯수를 세준다
            dfs(i) # 그리고 재귀
    

dfs(a)
print(visited)
if visited[b] != 0: # 방문하지 않은 노드는 아예 연결이 안되어있는 노드이기 때문에
    print(visited[b]) 
else:
    print(-1) # -1을 출력해준다.
