import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
dx = [1,-1,0,0]
dy = [0,0,1,-1]

for _ in range(n):
    # 그래프를 입력 받는다.
    graph.append(list(map(int,input().rstrip())))

# 3차원 리스트를 만들어 준다(벽을 부쉈는지 안부쉈는지 체크하는 부분이 추가됐다)
# visited=[행][열][벽을 부순 여부] 이런식이다
visited = [[[0]*2 for _ in range(m)] for _ in range(n)] 

def bfs(a,b,c):
    q=deque()
    q.append((a,b,c))
    visited[a][b][c] = 1
    
    while q:
        x,y,z = q.popleft()

        # 주어진 조건에 맞을경우 결과값을 리턴해준다.
        if x == n-1 and y == m-1:
            return visited[x][y][z]

        for i in range(4):
            nx = x + dx[i]
            ny = y + dy[i]

            if 0<=nx<n and 0<=ny<m:
                # 방문가능하며 벽을 아직 안부쉈다면
                if graph[nx][ny] == 0 and visited[nx][ny][z] == 0:
                    visited[nx][ny][z]=visited[x][y][z] + 1
                    q.append((nx,ny,z))
                # 벽이면서 부수지 않았다면
                elif graph[nx][ny] == 1 and z == 0:
                    # 벽을 부수고 진행
                    visited[nx][ny][z+1]=visited[x][y][z] + 1
                    q.append((nx,ny,z+1))
    return -1

print(bfs(0,0,0))

