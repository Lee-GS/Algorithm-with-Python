import sys
from collections import deque

input = sys.stdin.readline

T = int(input())

dx = [1,2,-1,-2,1,2,-1,-2] # 문제에 주어진 8개의 방향을 선언해준다.
dy = [2,1,2,1,-2,-1,-2,-1]

def bfs(a,b,x,y): #출발지점(a,b) 도착지점(x,y)를 파라미터로 잡아준다
    q=deque()
    q.append((a,b))
    visited[a][b] = 1 # 첫 스타트 지점을 1로 시작
    
    while q:
        x1,y1 = q.popleft()
        
        if x == x1 and y == y1: # popleft()의 좌표가 최종 목적지와 같을때 
            print(visited[x][y]-1) # -1을 하는 이유는 29번줄에서 더했기 때문에 빼줘야한다.
            break
        
        for i in range(8):
            nx = x1+dx[i]
            ny = y1+dy[i]
            
            if 0<=nx<I and 0<=ny<I and visited[nx][ny] == 0:
                q.append((nx,ny))
                visited[nx][ny] =visited[x1][y1]+1 # 좌표가 변경될때마다 +1씩 더해주며 최종목적지에 
                                                   # 도달했을때의 값을 출력해주면 최소 이동거리가 나온다.
    

for _ in range(T):
    I = int(input())
    a,b = map(int,input().split())
    x,y = map(int,input().split())
    
    visited = [[0]*I for _ in range(I)]
    bfs(a,b,x,y)
        
    
