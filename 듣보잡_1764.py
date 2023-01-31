n,m = map(int,input().split())
set1=set()
set2=set()

for _ in range(n):
    set1.add(input())
for _ in range(m):
    set2.add(input())
    
ans = sorted(list(set1&set2))

print(len(ans))
for i in range (len(ans)):
    print(ans[i])