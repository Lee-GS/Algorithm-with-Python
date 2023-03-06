import sys
input = sys.stdin.readline

n = int(input())
graph = [[0] for _ in range(n+1)]

for i in range(1,n+1):
    graph[i].append(map(int,input().split()))
