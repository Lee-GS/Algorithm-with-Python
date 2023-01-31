import sys
from collections import deque
input = sys.stdin.readline

N,L,R = map(int,input().split())

graph = []
#visited = [[0]*N for _ in range(N)]

dx = [-1,1,0,0]
dy = [0,0,1,-1]

for _ in range(N):
    graph.append(list(map(int,input().split())))

cnt = []
population = [[0]*N for _ in range(N)]

def bfs(a,b):
    list=[]
    visited = [[0]*N for _ in range(N)]
    population = [[0]*N for _ in range(N)]
    q=deque()
    q.append((a,b))
    visited[a][b] = 1
    if (L<=abs(graph[a][b]-graph[a+1][b])<=R or L<=abs(graph[a][b]-graph[a][b+1])<=R):
        population[a][b] =1
        list.append(graph[a][b]) 
            
    while q:
        x,y = q.popleft()

        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if (0<=nx<N and 0<=ny<N and visited[nx][ny] == 0):
                visited[nx][ny] = 1
                if L<=abs(graph[x][y]-graph[nx][ny])<=R:
                    population[nx][ny] = 1
                    list.append(graph[nx][ny])
                q.append((nx,ny))
    if len(list) != 0:
        new_population = sum(list)//len(list)
    
        print(new_population)
        for i in range (N):
            for j in range(N):
                if population[i][j] == 1:
                    graph[i][j] = new_population 
        cnt.append(1)
        print(population)
        if 1 in population:
            print(123)
            bfs(0,0)
        

bfs(0,0)

print(len(cnt))            
                        
    
