import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = []
visited = [[False]*(N) for _ in range(N)] # 방문 리스트 선언

dx=[1,-1,0,0] # 상하좌우
dy=[0,0,1,-1]

for _ in range(N):
    graph.append(list(input().rstrip())) # 그래프에 입력값 추가
    
def bfs(a,b,color):
    
    q=deque()
    q.append((a,b))
    
    while q:
        x,y=q.popleft()
        
        if visited[x][y] == False: #미방문일 경우
            visited[x][y] = True #방문처리 해준다
            for i in range(4): # 상하좌우 탐색
                nx = x + dx[i]
                ny = y + dy[i]
                if 0<=nx<N and 0<=ny<N and graph[nx][ny] == color: # 벽이나 범위 밖을 넘지 않고 색깔이 같다면
                    q.append((nx,ny)) # 데크에 바뀐 좌표를 추가

#적록색약이 아닐때
cnt=0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            color = graph[i][j] # 현재 위치의 색깔을 color 선언
            bfs(i,j,color)
            cnt+=1 #색깔 구역 카운트
print(cnt, end=" ")


#적록색약일때
visited = [[False]*(N) for _ in range(N)] # 적록색약일때 방문리스트 재선언
for i in range(N):
    for j in range(N):
        if graph[i][j] =='R': # R과G를 동일하게 변경 
            graph[i][j] = 'G'
        
#아래는 적록색약이 아닐때 설명과 동일
cnt_bg=0
for i in range(N):
    for j in range(N):
        if visited[i][j] == False:
            color = graph[i][j]
            bfs(i,j,color)
            cnt_bg+=1
print(cnt_bg)
        