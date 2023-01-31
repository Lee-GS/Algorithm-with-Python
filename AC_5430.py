import sys
from collections import deque
input=sys.stdin.readline

t = int(input())
reverse =0
for i in range (t):
    try:
        p = list(input().strip())
        n = int(input())
        arr = input()[1:-2].split(',')
        d=deque(arr)
        for k in range(len(p)):
            if p[k]=='R':
                reverse+=1
            elif p[k]=='D':
                d.popleft()
        if n<=0 or len(p)<=0:
            print("error")
        else:
            print('['+','.join(d)+']')           
    except:
        print("error")