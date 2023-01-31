import sys
from collections import deque
input = sys.stdin.readline

N = int(input())

graph = []

dx=[1,-1,0,0]#상하좌우
dy=[0,0,1,-1]

area_max = [] # 높이에 따른 안전구역수를 넣어줄 리스트

for _ in range(N):
    graph.append(list(map(int,input().split())))
    
list = sum(graph,[]) # 이중리스트를 1차원 리스트로 변경 
list = set(list) # 중복요소 제거

    
def bfs(a,b):
    q=deque()
    q.append((a,b))
    cnt = 0
    visited[a][b] = 0 #방문처리
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x + dx[i]    
            ny = y + dy[i]
            
            if 0<=nx<N and 0<=ny<N and visited[nx][ny] == 1:
                q.append((nx,ny)) # 좌표 추가
                visited[nx][ny] = 0 # 방문처리
                cnt+=1
    return cnt

def area():
    for i in range (N):
        for j in range(N):
            if visited[i][j] == 1:
                area_cnt.append(bfs(i,j)) # 안전구역을 넣어준다
    return len(area_cnt) # 안전구역의 총 수를 출력

for k in list : # 높이에 따라 구해줘야하기 때문에 높이를 담은 리스트로 반복해준다
    visited = [[1]*(N) for _ in range(N)] 
    area_cnt = [] # 안전구역의 갯수를 넣어줄 리스트
    for i in range (N):
        for j in range(N):
            if graph[i][j] < k:
                visited[i][j] = 0
    area_max.append(area()) # 높이에 따른 안전구역의 총 수가 들어가 있는 리스트
    
print(max(area_max)) # 각 높이중 가장 많은 안전구역이 들어있는 값을 출력



            

