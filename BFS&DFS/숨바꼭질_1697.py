import sys
from collections import deque

input = sys.stdin.readline
max = 100001
N,K = map(int,input().split())
count = [0]*max #시간초과가 나지 않게 크기를 설정해준다.

def bfs(a,b):
    q=deque()
    q.append(a)
    
    while q:
        x = q.popleft()
        if x == b:
            print(count[x])
            break
        for dx in (x-1,x+1,x*2): # 방향이 3개이므로 for문을 이렇게 선언해준다.
            if (0<=dx<max and count[dx] == 0): # 리스트보다 크지않고 방문 안했을때!!
                q.append(dx)
                count[dx] = count[x]+1 # 반복될때마다 1씩 더해준다.

bfs(N,K)