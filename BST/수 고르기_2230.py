import sys
input = sys.stdin.readline

n,m = map(int,input().split())
a = []
for _ in range(n):
    a.append(int(input()))

a.sort()
ans = 10e9

start = 0
end = 0

while start<n and end<n: # 리스트의 길이보다 작아야함
    if (a[end] - a[start]) < m: # m보다 작을경우 end를 늘려 값을 키워준다
        end+=1
    else:
        ans=min(ans,a[end]-a[start]) # m보다 크거나 같을경우 start를 늘려 범위를 다시 좁혀준다
        start+=1

print(ans)



