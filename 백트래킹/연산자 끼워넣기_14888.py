import sys
input = sys.stdin.readline

n = int(input())
a = list(map(int,input().split()))
sum,sub,mul,div = map(int,input().split())
max_value = -int(1e9) # -10억 -> 비교해줘야하는 수 이기 때문에 10억이 아닌 -10억으로 선언해준다
min_value = int(1e9) # 10억 -> 비교해줘야하는 수 이기 때문에 -10억이 아닌 10억으로 선언해준다


def dfs(sum,sub,mul,div,i,idx):
    global max_value, min_value
    if n == idx: # 모든 수가 다 사용됐을경우
        max_value = max(max_value,i) # 최댓값을 구한다
        min_value = min(min_value,i) # 최솟값을 구한다.
        return
    if sum > 0:
        dfs(sum-1,sub,mul,div,i+a[idx],idx+1)
        
    if sub > 0:
        dfs(sum,sub-1,mul,div,i-a[idx],idx+1)
        
    if mul > 0:
        dfs(sum,sub,mul-1,div,i*a[idx],idx+1)
        
    if div > 0:
        dfs(sum,sub,mul,div-1,int(i/a[idx]),idx+1)
        
dfs(sum,sub,mul,div,a[0],1)

print(max_value)
print(min_value)



