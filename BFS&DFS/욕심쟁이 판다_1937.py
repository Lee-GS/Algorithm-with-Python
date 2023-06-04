import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**9) # 재귀 깊이 설정

n = int(input())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

dp=[[0]*n for _ in range(n)] #dp리스트 선언

dx = [0,0,1,-1]
dy = [1,-1,0,0]

def dfs(x,y):
    if dp[x][y]:# 방문한적이 있다면 현재 값 리턴
        return dp[x][y]
    dp[x][y] = 1 # 방문한 적이 없다면 현재위치를 1로 선언
    for i in range(4): # 상하좌우 탐색
        nx = x+dx[i]
        ny = y+dy[i]

        if 0<=nx<n and 0<=ny<n and graph[x][y]<graph[nx][ny]:
            dp[x][y]=max(dp[x][y],dfs(nx,ny)+1) # 1 혹은 탐색한 값중 더 큰 값을 현재 위치에 넣어준다
    return dp[x][y]

ans = 0
for i in range(n):
    for j in range(n):
        ans=max(ans,dfs(i,j))

print(ans)
