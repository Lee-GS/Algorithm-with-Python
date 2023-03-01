n = int(input())
total = 0
graph = [[0]*101 for _ in range(101)] # 가로세로 100 크기의 그래프를 생성한다

for _ in range(n):
    a,b = map(int,input().split())

    for i in range(a,a+10): # 해당 범위에 가로세로를 10씩 더한값에
        for j in range(b,b+10): # 값을 1로 바꿔준다
            graph[i][j] = 1

for i in range(1,101):
    cnt = graph[i].count(1) # 1로 되어있는값을 갯수를 다 세어준후 total에 더해준다.
    total += cnt

print(total)