import sys
sys.setrecursionlimit(10**9)
input = sys.stdin.readline

graph = []
ans =[]
dx = [1,-1,0,0] # 상하좌우
dy = [0,0,1,-1] # 상하좌우

for _ in range(5):
    graph.append(list(map(str,input().split())))

def dfs(a,b,numbers):
    if len(numbers) == 6: # 길이가 6이고
        if numbers not in ans: # 해당 문자열이 ans에 들어있지 않을 경우
            ans.append(numbers) # 삽입
        return
    for i in range(4): # 현위치의 상하좌우를 찾아준다
            nx = a + dx[i]
            ny = b + dy[i]
            if 0<=nx<5 and 0<=ny<5: # 이동할 위치가 범위를 벗어나진 않는지 확인한다
                dfs(nx,ny,numbers+graph[nx][ny])# 다음 이동 위치를 재귀해주며 문자열을 늘려간다.

for i in range(5):
    for j in range(5):
        dfs(i,j,graph[i][j]) # for문을 돌리며 검사해준다.

print(len(ans))




