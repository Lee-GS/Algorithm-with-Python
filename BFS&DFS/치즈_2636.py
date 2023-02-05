import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
ans = []
hour = 0

for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(a,b):
    q=deque()
    q.append((a,b))
    visited[a][b] = True
    cnt=0
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if (0<=nx<n and 0<=ny<m and visited[nx][ny] == False):
                if graph[nx][ny] == 0:
                    visited[nx][ny] = True
                    q.append((nx,ny))
                elif graph[nx][ny] == 1:
                    graph[nx][ny] = 0
                    visited[nx][ny] = True
                    cnt+=1
    ans.append(cnt)
    return cnt


while True:
    visited = [[False]*m for _ in range(n)]
    hour+=1
    if bfs(0,0) == 0:
        break
    
print(hour-1)
print(ans[-2])
    
    
             
                    
                    