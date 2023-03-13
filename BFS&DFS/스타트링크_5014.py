from collections import deque
import sys
input = sys.stdin.readline

f,s,g,u,d = map(int,input().split())
count=[0]*(f+1)
visited = [False]*(f+1)

def bfs(S,G,U,D):
    q=deque()
    q.append(S)
    visited[S] = True

    while q:
        x = q.popleft()
        if x == G:
            print(count[x])
            break
        for nx in (x+U,x-D):
            if 0<nx<f+1 and visited[nx] == False :
                visited[nx] = True
                count[nx] = count[x]+1
                q.append(nx)
    
bfs(s,g,u,d)
if g != s and count[g] == 0:
    print("use the stairs")

        

