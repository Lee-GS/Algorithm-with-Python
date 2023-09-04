from collections import deque
def solution(rectangle, characterX, characterY, itemX, itemY):
    answer = 0
    graph = [[-1]*102 for _ in range(102)]
    dx = [1,-1,0,0]
    dy = [0,0,1,-1]
    
    for i in range(len(rectangle)):
        for j in range(rectangle[i][0]*2,(rectangle[i][2]*2+1)):
            for k in range(rectangle[i][1]*2,(rectangle[i][3]*2+1)):
                if rectangle[i][0]*2< j < rectangle[i][2]*2 and rectangle[i][1]*2 < k < rectangle[i][3]*2:
                    graph[k][j] = 0
                elif graph[k][j] != 0:
                    graph[k][j] = 1
                    
    def bfs(a,b):
        q=deque()
        q.append((a,b))
        
        while q:
            x,y = q.popleft()
            if x == itemY*2 and y == itemX*2:
                break
            for i in range(4):
                nx = x + dx[i]
                ny = y + dy[i]
                if  graph[nx][ny] == 1:
                    q.append((nx,ny))
                    graph[nx][ny] = graph[x][y]+1

    bfs(characterY*2,characterX*2)
    print(graph)
    answer = graph[itemY*2][itemX*2]//2
            
    return answer