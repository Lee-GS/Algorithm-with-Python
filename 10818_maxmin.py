import sys
n = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
print(min(a), end=' ')
print(max(a))