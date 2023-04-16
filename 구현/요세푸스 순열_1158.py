n,k = map(int,input().split())
arr = []
for i in range(1,n+1):
    arr.append(i)
tmp = []
while len(tmp)!=n:
    tmp.append(arr[k-1])
    arr.remove(arr[k-1])
    k+=k
    if k >= n:
        k=k-n
print(tmp)