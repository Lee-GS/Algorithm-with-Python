import sys
from collections import deque

input = sys.stdin.readline

M,N = map(int,input().split())

graph = []
visited = [[0]*M for _ in range(N)]
q=deque() # 데크 선언

dx = [1,-1,0,0] # 상하좌우 선언
dy = [0,0,1,-1]

for _ in range (N):
    graph.append(list(map(int,input().split()))) # 그래프 입력 받기
    
                
for i in range(N):
    for j in range(M):
        if graph[i][j] == 1: # 토마토가 익은 위치를 데크에 삽입
            q.append((i,j))
            
def bfs():
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if(0<=nx<N and 0<=ny<M and graph[nx][ny] == 0):
                q.append((nx,ny))
                graph[nx][ny] = graph[x][y]+1 # 현위치에서 이동할때마다 1씩 더해준다
                
bfs() # bfs 실행

count = 0 # 익을 수 업는 토마토의 갯수를 가운트 해줄 변수

for i in range (N): # bfs문이 실행되고나서 익지 못하는 토마토를 찾아 count++ 해준다
    for j in range (M):
        if graph[i][j] == 0:
            count+=1
            
if count == 0: # 익지 못한 토마토가 없을경우
    print(max(map(max,graph))-1)# 그래프에서 최대값을 찾아 -1을 해준다
                                # -1을 해주는 이유는 시작하는 부분은 빼야하기 때문이다.
else: # 익지 못한 토마토가 있을경우
    print(-1)
                