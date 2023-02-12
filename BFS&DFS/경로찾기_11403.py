import sys
input = sys.stdin.readline

sys.setrecursionlimit(10**9) # 재귀제한을 늘려주는건데 이문제에선 필요없다.

n = int(input())
graph = []
for i in range(n):
    graph.append(list(map(int,input().split())))

def dfs(V):
    for i in range(n):
        if visited[i] == 0 and graph[V][i] == 1:
            visited[i]=1
            dfs(i)

for i in range(n):#dfs문을 n 만큼 실행시켜준다.
    visited = [0]*(n) #visited에 dfs()가 실행되어 값들이 저장되어있다
                      # 돌릴때마다 초기화해준다.
    dfs(i)
    for j in range(n): # 저장되어 있는 값들을 출력형식에 맞게 출력해준다.
        if visited[j] == 1:
            print(1, end=' ')
        else:
            print(0,end=' ')
    print() #다음줄로~ 

