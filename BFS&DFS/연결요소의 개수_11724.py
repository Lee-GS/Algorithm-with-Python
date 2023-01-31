import sys
sys.setrecursionlimit(10**8) #재귀깊이제한을 늘렸다.
input = sys.stdin.readline

n,m=map(int,input().split())

graph=[[False]*(n+1) for _ in range(n+1)] # 노드들 간의 관계를 표시해줄 그래프 선언
visited = [False]*(n+1) # 방문 리스트 선언
cnt=0

for _ in range(m):
    x,y = map(int,input().split())
    graph[x][y]=graph[y][x]=True # 노드가 양방향 연결이기 때문에 스위칭해서 방문처리 해준다.\
            
def dfs(a):
    visited[a] = True # 시작한 노드 방문처리    
    for i in range(1,n+1):
        if visited[i] == False and graph[a][i] == True: # 방문하지 않았으며 인접노드가 방문처리 된 경우
            dfs(i)
            
for i in range(1,n+1):
    if visited[i] == False: #미방문 노드만 dfs문을 돌려 cnt를 늘려주며 연결요소의 개수를 카운트해준다.
        dfs(i)
        cnt+=1
        
print(cnt)