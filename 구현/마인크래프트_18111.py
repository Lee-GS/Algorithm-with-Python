import sys
input = sys.stdin.readline

n,m,b = map(int,input().split())

mine = []

for _ in range(m):
    mine.append(list(map(int,input().split())))
    