import sys
input = sys.stdin.readline

n,k = map(int,input().split())

line = list(input())
visited = [False]*n

for i in range(n):
    if line[i] == 'P':
        for j in range(i-k,i+k+1):
            if i==j or j<0 or j>=n:
                continue
            else:
                if visited[j] == False and line[j] == 'H':
                    visited[j] = True
                    break

print(visited.count(True))
