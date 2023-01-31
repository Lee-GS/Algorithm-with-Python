import sys
input = sys.stdin.readline

T = int(input())

for _ in range(T):
    test=list(map(int,input().split()))
    test.sort()
    print(test[7])