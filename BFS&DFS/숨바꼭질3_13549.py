import sys
from collections import deque
input = sys.stdin.readline

n,k = map(int,input().split())

limit = 100001 # 최대 범위 설정
count = [0]*limit
visited = [False]*limit

def bfs():
    q=deque() # 데크 선언
    q.append(n) # 데크 삽입

    while q:
        x = q.popleft() # 데크에서 값을 꺼낸다

        if 0<=2*x<limit and visited[2*x] == False: # 2배인 경우는 초가 늘어나지 않으므로 따로 처리
            visited[2*x] = True # 방문처리
            count[2*x] = count[x] # 이동위치에 이동 전 값을 대입
            q.append(2*x) 

        for dx in (x-1,x+1): # -1,+1인 경우는 1초가 늘어나므로 검사해준다.
            if 0<=dx<limit and visited[dx] == False:
                q.append(dx)
                count[dx]=count[x]+1 #이동 전 값에 +1초를 해준후 이동 후 값에 대입
                visited[dx] =  True # 방문 처리

if n == k: # 시작점과 도착점이 같다면 0초를 출력
    print(0)
else:
    bfs()
    print(count[k])


