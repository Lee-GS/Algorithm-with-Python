import sys
input = sys.stdin.readline

n,s = map(int,input().split())
array = list(map(int,input().split()))
visited = [False] * n
ans = []
total = 0

def dfs():
    global total
    if len(ans) != 0:
        if sum(ans) == s and sorted(ans) == ans:
            total+=1 
    for i in range(len(array)):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(array[i])
        dfs()
        ans.pop()
        visited[i] = False

dfs()
print(total)