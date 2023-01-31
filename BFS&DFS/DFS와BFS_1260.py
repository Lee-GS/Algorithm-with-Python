from collections import deque

N,M,V = map(int,input().split())

graph = [[False]*(N+1) for _ in range(N+1)]

for _ in range (M):
    a,b =  map(int,input().split())
    graph[a][b] = True #서로 연결된부분은 
    graph[b][a] = True #둘다 True로 변형해준다
    
visited_dfs = [False]*(N+1) # 미방문 리스트를 만든다
visited_bfs = [False]*(N+1) # 범위가 N+1인 이유는 이해하기 쉽게 [0]이 첫번째가 아닌 [1]이 첫번째로 하기 위해서이다.

def dfs(V):
    visited_dfs[V] = True # 시작 노드를 방문처리 해준다
    print(V, end=" ") 
    for i in range(1,N+1):
        if (visited_dfs[i] == False and graph[V][i] == True): # 방문하지 않았으며 True 바뀐 노드와 인접한경우!
            dfs(i) # 재귀호출!
            
def bfs(V):
    q = deque([V]) #데크를 쓰는 이유는 출입구가 양쪽에 있기 때문에 빠른 데이터 처리가 가능하기 때문이다
    visited_bfs[V] = True # 시작 노드 방문처리
    while q: # q가 빌때까지
        V = q.popleft() #방문한 노드를 V에 대입
        print(V, end=" ") 
        for i in range(1,N+1): 
            if visited_bfs[i] == False and graph[V][i] == True: # 위의 DFS 설명과동일
                q.append(i) # 데크에 추가해준다
                visited_bfs[i] = True # 그리고 방문처리

dfs(V)
print()
bfs(V)                            