import sys
import copy
input = sys.stdin.readline

n = int(input())
graph = [[0]*(n) for _ in range(n)] 

dx = [1,-1,0,0]
dy = [0,0,1,-1]



def rule1(tmp):
    ans = 0
    for i in range(n):
        for j in range(n):
            cnt = 0
            if graph[i][j] == 0:
                for k in range(4):
                    nx = i+dx[k]
                    ny = j+dy[k]
                    if 0<=nx<n and 0<=ny<n and graph[nx][ny] in arr :
                        cnt+=1
                if ans < cnt:
                    tmp.clear()
                    tmp.append([i,j])
                    ans=cnt
                elif ans == cnt:
                    tmp.append([i,j])

def rule2(tmp2,arr3):
    ans = 0
    for i in tmp2:
        cnt=0
        for k in range(4):
            nx = i[0]+dx[k]
            ny = i[1]+dy[k]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] == 0:
                cnt+=1
        if ans < cnt:
            arr3.clear()
            arr3.append(i)   
            ans=cnt
        elif ans == cnt:
            arr3.append(i)

arr10 = []
for i in range(n*n):
    arr = list(map(int,input().split()))
    arr2 = []
    arr7 = []

    rule1(arr2)
    
    if len(arr2)>1:
        rule2(arr2,arr7)
        graph[arr7[0][0]][arr7[0][1]] = arr[0]
    else:
        graph[arr2[0][0]][arr2[0][1]] = arr[0]

    arr11 = copy.deepcopy(arr)
    arr10.append(arr11)

arr10.sort()
answer = 0
for i in range(len(arr10)):
    del arr10[i][0]

for i in range(n):
    for j in range(n):
        cnt = 0
        for l in range(4):
            nx = i + dx[l]
            ny = j + dy[l]
            if 0<=nx<n and 0<=ny<n and graph[nx][ny] in arr10[graph[i][j]-1]:
                cnt+=1
        if cnt == 0:
            answer += 0
        else:
            answer += 10**(cnt-1)
        
print(answer)
     



    