N,K = map(int,input().split())
arr = []
for i in range(1,N+1):
    arr.append(i)
num = 0
ans =[]

for i in range(N):
    num+=(K-1)
    if num >= len(arr):
        num %= len(arr)
    ans.append(str(arr[num]))
    arr.pop(num)

print("<",', '.join(ans),">", sep="")