import sys
from collections import deque

input = sys.stdin.readline

n,m = map(int,input().split())

graph = []

dx = [0,0,1,-1]
dy = [1,-1,0,0]
for _ in range(n):
    graph.append(list(input()))

def bfs(a,b):
    visited = [[0]*m for _ in range(n)] #몇시간 걸릴지 세는 리스트 선언
    q=deque()
    q.append((a,b))
    visited[a][b] = 1
    cnt = 0 #시간을 비교해줄 cnt 선언
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]

            if 0<=nx<n and 0<=ny<m and graph[nx][ny]=='L' and visited[nx][ny] == 0:
                visited[nx][ny] = visited[x][y]+1
                cnt = max(cnt,visited[nx][ny]) #cnt엔 가장 높은 시간만 들어가야 함으로 탐색할때마다 비교해준다
                q.append((nx,ny))
    return cnt # 결과적으론 가장 오래 걸린 시간이 return 된다

answer = 0

for i in range(n):
    for j in range(m):
        if graph[i][j] == 'L':
            answer = max(answer,bfs(i,j)-1) # 전체 좌표를 돌면서 bfs 문을 실행해 주어 가장 오래걸린 시간을 찾아낸다
                                            # -1 을 해준 이유는 시작 지점을 포함해서 계산했기 때문에 마지막에 -1을 해준거다 

print(answer)


