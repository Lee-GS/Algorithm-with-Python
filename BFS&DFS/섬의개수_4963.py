import sys
from collections import deque

input = sys.stdin.readline

def bfs(a,b):
    q=deque()
    q.append((a,b))
    graph[a][b]=0 # 방문처리
    
    while q:
        x,y = q.popleft()
        
        for i in range(8): # 8개의 방향을 탐색
            nx = x + dx[i]
            ny = y + dy[i]
            
            if (0<=nx<h and 0<=ny<w and graph[nx][ny] == 1): # 벽에 안닿고 가야할 방향에 미방문일때
                q.append((nx,ny)) # 가야할 방향을 큐에 추가
                graph[nx][ny]=0 # 방문처리

dx = [1,-1,0,0,1,1,-1,-1] #상하좌우 대각선까지  
dy = [0,0,1,-1,1,-1,1,-1] # 총 8개의 방향을 선언

q1 = deque() # 입력 예제와 같게하기 위해 큐를 하나 생성
q1.append(map(int,input().split())) # 첫번째 입력

while q1: # 입력 예제가 빌때까지 반복
    cnt=0
    graph = []
    w,h = q1.popleft()
    if w == 0 and h == 0: # 0,0이 입력되면 종료
        break
    for _ in range(h):
        graph.append(list(map(int,input().split()))) # 그래프 입력
    for i in range(h):
        for j in range(w):
            if graph[i][j] == 1: # 그래프탐색
                bfs(i,j)
                cnt+=1
    print(cnt) # 정답 출력
    q1.append(map(int,input().split())) #다음 입력을 이어서해준다
        
    
        