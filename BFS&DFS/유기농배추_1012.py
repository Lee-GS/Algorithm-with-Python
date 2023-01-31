import sys
from collections import deque

T=int(input())

dx = [1,-1,0,0] #상하
dy = [0,0,1,-1] #좌우

def bfs(graph,a,b):
    q=deque()
    q.append((a,b))
    graph[a][b] = 0 # 방문처리
    cnt=1 # 1을 지날때마다 하나씩 카운트
    
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<M and 0<=ny<N and graph[nx][ny] == 1: # 벽이 아니고 지나갈수있는 1 표시일때!
                graph[nx][ny]=0 # 방문처리
                q.append((nx,ny))
                cnt+=1 # 카운트 쁠쁠
    return cnt

for _ in range(T):
    
    M,N,K = map(int,input().split())
    graph = [[0]*(N) for _ in range(M)]
    count =[]
    for _ in range(K):
        X,Y = map(int,input().split())
        graph[X][Y]=1
        
    for i in range(M):
        for j in range(N):
            if graph[i][j] == 1:
                count.append(bfs(graph,i,j)) # count리스트에 cnt 값을 추가해준다
    
    print(len(count)) # [3,2,2,1,6]으로 count리스트가 되 있을거다.
                      # 그러고 count 길이를 출력해주면 된다   