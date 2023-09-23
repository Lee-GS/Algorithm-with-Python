import sys, copy
from  collections import deque
from itertools import combinations
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]
wall = []
q = deque()
ans = -1e9

def bfs():
    while q2:
        x,y = q2.popleft()

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]
            if 0<=nx<n and 0<=ny<m and visited[nx][ny] == False and graph2[nx][ny] == 0:
                visited[nx][ny] = True
                graph2[nx][ny] = 2
                q2.append((nx,ny))

for  _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n):
    for j in range(m):
        if graph[i][j] == 0:
            wall.append((i,j))
        elif graph[i][j] == 2:
            q.append((i,j))

tmp = list(combinations(wall,3))

for i in range(len(tmp)):
    graph2 = copy.deepcopy(graph)
    q2 = copy.deepcopy(q)
    visited = [[False]*m for _ in range(n)]
    res = 0
    for j in range(len(tmp[0])):
        x,y = tmp[i][j]
        graph2[x][y] = 1
    bfs()
    for k in range(n):
        for l in range(m):
            if graph2[k][l] == 0:
                res+=1
    ans = max(ans,res)

print(ans)