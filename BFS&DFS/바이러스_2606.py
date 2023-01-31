n = int(input())
m = int(input())

graph = [[0]*(n+1) for _ in range(n+1)]

for _ in range(m):
    a,b = map(int,input().split())
    graph[a][b] = graph[b][a] = 1

visited = [0]*(n+1)

def dfs(v):
    visited[v] = 1
    print(visited)
    for i in range(n+1):
        if graph[i][v] == 1 and visited[i] == 0:
            dfs(i)
            
print(graph)
dfs(1)

print(sum(visited)-1)