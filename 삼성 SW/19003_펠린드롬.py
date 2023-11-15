from itertools import combinations

tc = int(input())

def pelindrom(tmp):
    if tmp == tmp[::-1]:
        return True
for _ in range(tc):
    n,m = map(int,input().split())
    arr = []
    cnt = 0
    for i in range(n):
        arr.append(input())
    for i in range(1,len(arr)+1):
        for k in combinations(arr,i):
            tmp = ''.join(k)
            if  pelindrom(tmp):
                cnt = max(cnt,len(tmp))
    print(cnt)