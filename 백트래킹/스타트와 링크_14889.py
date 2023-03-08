import sys
input = sys.stdin.readline

n = int(input())
graph = []
start = []
ans = int(1e9)

for i in range(n):
    graph.append(list(map(int,input().split())))

visited = [False]*n

def dfs(depth,idx):
    global ans
    if len(start) == n//2:
        start_value = 0
        link_value = 0
        for i in range(n):
            for j in range(n):
                if visited[i] and visited[j]:   
                    start_value += graph[i][j]
                elif not visited[i] and not visited[j]:
                    link_value += graph[i][j]
    
        ans=min(ans,abs(start_value-link_value))
        return
    
    for i in range(idx, n):
        if not visited[i]:
            visited[i] = True
            dfs(depth+1, i+1)
            visited[i] = False


dfs(0,0)
print(ans)


