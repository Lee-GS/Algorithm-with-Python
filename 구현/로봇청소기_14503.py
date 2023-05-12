import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
r,c,d = map(int,input().split())

graph = []
visited = [[False]*m for _ in range(n)]
dx=[1,-1,0,0]
dy=[0,0,1,-1] 
for _ in range(n):
    graph.append(list(map(int,input().split())))

def bfs(a,b):
    q=deque()
    q.append((a,b))
    visited[a][b]=True

    while q:
        x,y = q.popleft()

        

