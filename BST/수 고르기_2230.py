import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
ans = []

def bs(array,target,start,end):
    if start>end:
        return None
    mid = (start+end)//2
    if (array[end]-array[start])>=target:
        ans.append(array[end]-array[start])
        return bs(array,target,start,mid)
    else:
        return bs(array,target,mid+1,end)

bs(a,m,0,len(a)-1)
print(min(ans))
    


