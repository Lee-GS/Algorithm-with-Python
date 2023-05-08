import sys
import itertools
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
chicken = []
for _ in range(n):
    graph.append(list(map(int,input().split())))

for i in range(n): # 치킨집 좌표를 찾아주는 for문 입니다.
    for j in range(n):
        if graph[i][j] == 2:
            chicken.append((i,j))
        
final_chicken = list(itertools.combinations(chicken,m)) # 남아 있어야 하는 치킨집의 경우의 수를 구합니다.

tmp = []
for x in final_chicken: # 남아있는 치킨집에 대해 치킨거리가 가장낮은 경우를 찾아줍니다.
    distance = 0
    for i in range(n):
        for j in range(n):
            if graph[i][j] == 1: # 집을 발견했을때
                value = 10e9
                for a in x:# 예제 1의 경우 x = [(1,2),(2,2),(4,4)]로 되어 있으므로 집들을 앞의 3개의 치킨집에 계산해 가장 낮은 치킨거리를 찾는다
                    total=abs(i-a[0])+abs(j-a[1])
                    value = min(total,value)
                distance+=value #distance라는 변수에 모든 집의 치킨거리를 더해줘 해당 경우의 수가 갖는 최소 치킨거리를 tmp리스트에 넣어준다.
    tmp.append(distance)
print(min(tmp)) # 모든 경우의 수의 가장낮은 치킨거리를 출력해준다!
