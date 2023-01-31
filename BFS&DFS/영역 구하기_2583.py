import sys
from collections import deque
input = sys.stdin.readline

M,N,K = map(int,input().split())


visited = [[1]*N for _ in range(M)] # 0 이아닌 1로 한 이유는 입력 받을 값을 0 으로 바꿔줄거이기 때문이다.
dx=[1,-1,0,0]
dy=[0,0,1,-1]
area=[]

for _ in range (K):
    x1,y1,x2,y2 = map(int,input().split()) # 값들을 입력 받는다
    for i in range(y1,y2): 
        for j in range (x1,x2):
            if visited[i][j] == 1: # 중복되는 부분이 있을수 있기에 조건문을 넣어준다.
                visited[i][j] = 0
                
def bfs(a,b):
    q = deque()
    q.append((a,b))
    visited[a][b] = 0
    cnt=1 #bfs 문이 돌때마다 좌표의 갯수를 카운트 해줘야 한다.
    while q:
        x,y = q.popleft()
        
        for i in range(4):
            nx = x+dx[i]
            ny = y+dy[i]
            
            if 0<=nx<M and 0<=ny<N and visited[nx][ny]==1:
                q.append((nx,ny))
                visited[nx][ny] = 0
                cnt+=1
    return cnt # 좌표의 갯수 카운트

# 전체적으로 for 문을 돌면서 bfs 문을 돌려준다
for i in range(M):
    for j in range(N):
       if visited[i][j] == 1:# 방문이 가능한 곳만 돌려준다
            area.append(bfs(i,j)) # 그렇게 나온 좌표의 갯수를 area 리스트에 넣어준다

# 결과 출력
print(len(area))
area.sort()
for i in area:
    print(i, end=" ")

    