import sys
input = sys.stdin.readline

n,s = map(int,input().split())
array = list(map(int,input().split()))
ans = []
total = 0

def dfs(start):
    global total
    if sum(ans) == s and len(ans)>0:
        total+=1 
    for i in range(start,n):     
        ans.append(array[i])
        dfs(i+1)
        ans.pop()

dfs(0)
print(total)