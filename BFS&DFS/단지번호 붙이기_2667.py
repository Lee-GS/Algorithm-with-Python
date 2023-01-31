import sys
from collections import deque

N = int(input())

graph = []
for _ in range(N):
    graph.append(list(map(int,sys.stdin.readline().rstrip())))
    
dx = [-1,1,0,0]
dy = [0,0,1,-1]

def bfs(a,b):
    q = deque()
    q.append((a,b))
    graph[a][b] = 0
    cnt=1
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<N and 0<=ny<N and graph[nx][ny] == 1:
                graph[nx][ny] = 0
                q.append((nx,ny))
                cnt+=1
    return cnt


count = []
for i in range(N):
    for j in range(N):
        if graph[i][j] == 1:
            count.append(bfs(i,j))

count.sort()
print(len(count))

for i in range(len(count)):
    print(count[i])                