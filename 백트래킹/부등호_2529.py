import sys
input = sys.stdin.readline

k = int(input())
arr = list(input().split())
visited = [False]*10

ans = []
"""tmp = []

def dfs():
    if len(ans) == k+1:
        check = [False]*k
        for i in range(k):
            if arr[i] == '>':
                if ans[i]>ans[i+1]:
                    check[i] = True
                    continue
                else:
                    break
            else:
                if ans[i]<ans[i+1]:
                    check[i] = True
                    continue
                else:
                     break
        if False not in check:
            tmp.append(''.join(map(str,ans)))
        return
    for i in range(10):
        if visited[i]:
            continue
        visited[i]=True
        ans.append(i)
        dfs()
        ans.pop()
        visited[i]=False

dfs()
print(max(tmp))
print(min(tmp))"""

def check_up(i, j, k): # True, False를 판단해줄 함수
    if k == '<':
        return i < j
    else:
        return i > j

def dfs(iter, temp):
    if iter == k + 1: # 문자열의 길이가 k+1의 자리가 될 때
        ans.append(temp)
        return

    for i in range(10):
        if not visited[i]:
            # 문자열의 길이가 0이거나 부등호의 수식이 True일때
            if iter == 0 or check_up(temp[-1], str(i), arr[iter - 1]): 
                visited[i] = 1
                dfs(iter + 1, temp + str(i)) # 다음 수식들을 또 검사해준다
                visited[i] = 0
dfs(0, "")

print(ans[-1])
print(ans[0])