import sys
input = sys.stdin.readline

n,m = map(int,input().split())

visited = [False] * n # 방문 리스트

graph = [[] for _ in range(n)] # 그래프
answer = False # 친구관게가 4단계인지 아닌지 판별 해줄 변수

for _ in range(m):
    a,b = map(int,input().split())
    # 양방향 연결이므로 양쪽 리스트에 다 넣어준다.
    graph[a].append(b)
    graph[b].append(a)

def dfs(x,depth):
    global answer
    visited[x] = True
    if depth == 4: # 관계가 4까지 다달으면 조건 성립함으로
        answer = True # true로 바꿔준다
        return 
    for i in graph[x]: # 그래프안에 있는 변수를 검사해준다
        if visited[i] == False: # 방문하지 않은 노드이면
            dfs(i,depth+1) # 해당 노드를 검사하고 depth를 1증가 시켜준다.
    visited[x] = False # 4까지 도달하지 못한 경우 이므로 다시 false로 바꾸어준다.

for i in range(n):# 노드를 검사해준다
    dfs(i,0)
    if answer == True:
        break

if answer:
    print(1)
else:
    print(0)
    
