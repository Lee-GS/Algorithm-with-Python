import sys
n,m= map(int,sys.stdin.readline().split())

arr1 = []
arr2 = []

for i in range(m):
    a,b = map(int,sys.stdin.readline().split())
    arr1.append(a)
    arr2.append(b)
min1=min(arr1)
min2=min(arr2)

if min1<min2*6:
    if min1<(n%6)*min2:
        print((n//6)*min1+min1)
    else:
        print((n//6)*min1+(n%6)*min2)
elif min1>=min2*6:
    print(n*min2)
