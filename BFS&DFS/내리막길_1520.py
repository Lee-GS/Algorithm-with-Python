import sys

input = sys.stdin.readline

graph = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]
n,m = map(int,input().split())
dp = [[-1]*m for _ in range(n)] # dp 테이블 선언

for _ in range(n):
    graph.append(list(map(int,input().split())))



def dfs(a,b):
    if a == n-1 and b == m-1: # 목적지에 다다르면
        return 1 # 1을 리턴
    if dp[a][b] == -1: # 미방문한곳이면
        dp[a][b] = 0 # 방문처리

        for i in range(4): # 상하좌우 탐색
            nx = a+dx[i]
            ny = b+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[a][b]>graph[nx][ny]: 
                dp[a][b]+=dfs(nx,ny) # 현 위치에 저장되어 있던 값을 더해준다.
    return dp[a][b] 

print(dfs(0,0))
