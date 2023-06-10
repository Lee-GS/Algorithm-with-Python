n = int(input())

cnt = 0
graph = [0] * n

def check(b):
    for i in range(b):
        if graph[i] == graph[b] or abs(graph[b]-graph[i]) == abs(b-i):
            return False
        
    return True

def dfs(a):
    global cnt
    if a == n:
        cnt+=1
    else:
        for i in range(n):
            graph[a] = i
            if check(a):
                dfs(a+1)

dfs(0)
print(cnt)

