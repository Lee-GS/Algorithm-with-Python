import sys
n,x = map(int,sys.stdin.readline().split())
a = list(map(int,sys.stdin.readline().split()))
ans = []
for i in range(n):
    if(x>a[i]):
        ans.append(a[i])
for j in range(len(ans)):
    print(ans[j], end=' ')       
        
        