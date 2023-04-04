import sys
input = sys.stdin.readline

n,s = map(int,input().split())
array = list(map(int,input().split()))
ans = []
total = 0 

def dfs(start):
    global total
    if sum(ans) == s and len(ans)>0: # 합이 s와 같고 길이는 0보다 커야한다.
        total+=1 
    for i in range(start,n): # 모든 부분 수열을 검사해줄 for문이다.
        ans.append(array[i])
        dfs(i+1) # 다시 다음 위치부터 또 다른 부분수열을 검사한다.
        ans.pop() # 검사가 끝나고 더이상 넣을게 없다면 pop()시켜준다

dfs(0)
print(total)