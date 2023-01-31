import sys

a,b=sys.stdin.readline().split()

ans = []

for i in range(len(b)-len(a)+1):
    cnt = 0
    for k in range(len(a)):
        if(a[k]!=b[i+k]):
            cnt=cnt+1
    ans.append(cnt)
    
print(min(ans))
