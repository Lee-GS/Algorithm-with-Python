from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())
count=[0]*(f+1) # 계단 
visited = [False]*(f+1) # 방문처리할 리스트

def bfs(S,G,U,D):
    q=deque() # 데크 선언
    q.append(S) # 처음 위치를 삽입
    visited[S] = True # 처음위치 방문처리

    while q:
        x = q.popleft()
        if x == G: # 스타트 링크의 층과 같으면
            print(count[x]) # 출력
            break
        for nx in (x+U,x-D): # 현위치에서 위로갈 층, 아래로갈 층을 탐색한다
            if 0<nx<f+1 and visited[nx] == False: # 범위 안벗어나고 방문하지 않았으면
                visited[nx] = True # 방문처리 해준다
                count[nx] = count[x]+1 # 움직일때마다 +1씩 늘려준다
                q.append(nx) # 데크 삽입
    
bfs(s,g,u,d)
if g != s and count[g] == 0: # 처음시작할때 같은 위치에 있지 않거나 스타트 층을 방문하지 않았을때
    print("use the stairs")

        

