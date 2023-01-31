import sys
n = int(input())
a = list(map(int,sys.stdin.readline().split()))
b = list(map(int,sys.stdin.readline().split()))
s=0
total=0
a.sort()
b.sort(reverse=True)

for i in range(n):
   s=a[i]*b[i]
   total=total+s
    
print(total)