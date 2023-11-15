tc = int(input())

def bfs(a,b):
    dx = [0,0,1,-1]
    dy = [1,-1,0,0]

    for i in range(4):
        nx = a+dx[i]
        ny = b+dy[i]
        for l in range(1,8):
            nx = a+dx[i]
            nx=nx*l
            if 0<=nx<8 and 0<=ny<8 and graph[nx][ny] == 'O':
                return False
        nx = a+dx[i]
        for l in range(1,8):
            ny = b+dy[i]
            ny=ny*l
            if 0<=nx<8 and 0<=ny<8 and graph[nx][ny] == 'O':
                return False



for i in range(1,tc+1):
    graph = []
    for _ in range(8):
        graph.append(list(input()))
    flag = True
    for x in range(8):
        for y in range(8):
            if graph[x][y]=='O' and bfs(x,y) == False:
                flag = False
                break
        if flag == False:
            break
    answer = []
    for element in graph:
        answer+=element
    if flag:
        print(f'#{i} {"yes"}')
    elif answer.count('.') == 64:
        print(f'#{i} {"no"}')
    else:
        print(f'#{i} {"no"}')