
r,c = map(int,input().split())
graph = [list(input()) for _ in range(r)]

x = (1,-1,0,0)
y = (0,0,1,-1)
count = set()
cnt = 0

def dfs(a,b,c):
    global cnt 
    cnt = max(c,cnt)
    count.add(graph[a][b])

    for i in range(4):
        nx = a+x[i]
        ny = b+y[i]
        
        if(0<=nx<r and 0<=ny<c):
            if graph[nx][ny] not in count :
                dfs(nx,ny,c+1)
                
    count.remove(graph[a][b])

    
dfs(0,0,1)

print(cnt)
