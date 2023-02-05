import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
dx = [1,-1,0,0] #상하
dy = [0,0,1,-1] #좌우
ans = [] 
hour = 0

for _ in range(n):
    graph.append(list(map(int,input().split()))) # 그래프 입력 받기

def bfs(a,b):
    q=deque() # 데크 선언
    q.append((a,b))
    visited[a][b] = True # 방문처리
    cnt=0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if (0<=nx<n and 0<=ny<m and visited[nx][ny] == False):
                # !!!!아래부분이 이번 문제의 핵심 알고리즘이다.!!!!
                
                if graph[nx][ny] == 0: # 방문한곳이 공기일 경우
                    visited[nx][ny] = True # 그냥 방문처리만 해준다
                    q.append((nx,ny)) # 그러고 다시 치즈를 찾아 탐색한다.
                    
                elif graph[nx][ny] == 1: # 그러나!!! 방문하곳이 치즈일경우
                    graph[nx][ny] = 0 # 치즈였던 부분을 공기로 바꿔주고
                    visited[nx][ny] = True # 방문처리를 해준다
                    cnt+=1 # 그러고 치즈의 개수를 +1 해준다.
                    
                    
                    # 위의 elif 부분에서는 q에 다시 append해 주지 않았다.
                    # 이유는 탐색을 공기에서 시작해 치즈에서 만나는 곳에서 끝내야 함으로
                    # q에 추가해주지 않은것이다.
                    # 그래야 가장자리에 있는 치즈만 탐색 할 수 있다.
                    
    ans.append(cnt)
    return cnt


while True:
    visited = [[False]*m for _ in range(n)]
    hour+=1
    if bfs(0,0) == 0:
        break
    
print(hour-1)
print(ans[-2])
    
    
             
                    
                    