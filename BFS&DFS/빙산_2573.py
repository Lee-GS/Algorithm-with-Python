import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
dy = [0,0,1,-1]
dx = [1,-1,0,0]

for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(a,b): # 일반적인 bfs 입니다.
    q=deque()
    q.append((a,b))
    visited[a][b]=True
    cnt=1

    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny] != 0 and visited[nx][ny] == False:
                visited[nx][ny]=True
                q.append((nx,ny))
                cnt+=1
    return cnt

def check_glacier():# 1년이 지날때 마다 빙하의 높이를 갱신해주는 함수입니다.
    mountain = [[0]*m for _ in range(n)]
    for i in range(n):
        for j in range(m):
            ice = 0
            if graph[i][j] != 0:
                for k in range(4):
                    if graph[i+dx[k]][j+dy[k]] == 0: # 해당위치의 상하좌우에 0이 몇개있는지 검사합니다.
                        ice+=1
                mountain[i][j]=ice # mountain 리스트에 해당위치의 0과 인접한 갯수를 넣어줍니다.
    for i in range(n): # 초기의 graph에서 mountain의 값을 빼줍니다. -> 1년 후의 빙산의 모습이 생깁니다.
        for j in range(m):
            if graph[i][j] - mountain[i][j]>0:
                graph[i][j]-=mountain[i][j]
            else:
                graph[i][j] = 0
    
year = 1 
glacier = []
flag=0
while True:
    glacier = []
    visited = [[False]*m for _ in range(n)]
    check_glacier() # 1년후의 빙하를 계산합니다
    for i in range(n):
        for j in range(m):
            if graph[i][j] != 0 and visited[i][j] == False:
                glacier.append(bfs(i,j)) # 빙하 섬의 갯수를 넣어줍니다
    if len(glacier) == 0:
        break
    if len(glacier) >= 2:
        flag=1
        break
    year+=1

if flag == 1:
    print(year)
else:
    print(0)


        


        