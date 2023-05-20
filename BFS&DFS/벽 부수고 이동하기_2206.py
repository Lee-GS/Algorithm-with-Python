import sys
from collections import deque
input = sys.stdin.readline

n,m = map(int,input().split())
graph = []
for _ in range(n):
    graph.append(list(map(int,input().split())))