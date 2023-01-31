import copy
import sys
n = int(sys.stdin.readline())
d = [0]*41
d[1] = 1
d[2] = 1
def fibo(x):
    if x == 1 or x == 2:
        return 1
    if x == 0:
        return 0
    if d[x] != 0:
        return d[x]
    d[x] = fibo(x-1) + fibo(x-2)
    return d[x]

for i in range (n):
    x =int(sys.stdin.readline())
    fibo(x)
    d2 = copy.deepcopy(d)
    d2.insert(0,1)
    print(d2[x],d[x])
    

    
    