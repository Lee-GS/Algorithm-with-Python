import sys
input = sys.stdin.readline

n,m = map(int,input().split())

tetris = []

for _ in range(n):
    tetris.append(list(map(int,input().split())))

visited = [[False]*m for _ in range(n)]
max_value = max(map(max,tetris))
dx = [1,-1,0,0]
dy = [0,0,1,-1]

ans = 0

def dfs(a,b,total,step):
    global ans
    if ans >= total+max_value*(4-step):
        return
    if step == 4:
        ans = max(ans,total)
        return
    else:
        for i in range(4):
            nx = a + dx[i]
            ny = b + dy[i]

            if 0<=nx<n and 0<=ny<m and visited[nx][ny]==False:
                if step == 2:
                    visited[nx][ny] = True
                    dfs(a,b,total+tetris[nx][ny],step+1)
                    visited[nx][ny] = False
                visited[nx][ny] = True
                dfs(nx,ny,total+tetris[nx][ny],step+1)
                visited[nx][ny] = False
            
for i in range(n):
    for j in range(m):
        visited[i][j] = True
        dfs(i,j,tetris[i][j],1)
        visited[i][j] = False
print(ans)