def solution(n, computers):
    answer = 0
    ans = []
    graph =[[0]*n for _ in range(n)]
    visited = [False]*(n)

    for i in range(n):
        for j in range(n):
            if i != j and computers[i][j] == 1:
                graph[i][j]=graph[j][i]=1
    
    def dfs(i):
        cnt = 0
        visited[i]=True
        cnt+=1
        for k in range(n):
            if graph[i][k] == 1 and visited[k] == False:
                dfs(k)
        return cnt
    
    for i in range(n):
        if visited[i]==False:
            ans.append(dfs(i))
    
    answer = len(ans)
                
            
    return answer

