import sys 
input = sys.stdin.readline

n =  int(input())
city = []
cost = []
tmp = []
visited = [False]*n
for i in range(n):
    city.append(list(map(int,input().split())))


def dfs(idx):
    if idx == n:
        tmp.append(tmp[0])
        value = 0
        for j in range(n):
            if city[tmp[j]][tmp[j+1]] == 0 and min(cost) < city[tmp[j]][tmp[j+1]]:
                tmp.pop()
                return
            value+=city[tmp[j]][tmp[j+1]]
        cost.append(value)
        tmp.pop()
        return
    for i in range(n):
        if visited[i]:
            continue
        visited[i] = True
        tmp.append(i)
        dfs(idx+1)
        tmp.pop()
        visited[i] = False

dfs(0)

print(min(cost))
