import sys 
input = sys.stdin.readline

n = int(input())
arr = list(map(int,input().split()))
visited = [False]*n
arr2 = []
ans = 0

def dfs():
    global ans
    total = 0
    if len(arr2) == n: # 길이가 n이 되었을때 
        for i in range(n-1):
            total += abs(arr2[i]-arr2[i+1]) # 조건에 나와있는 수식을 실행해준다
        ans = max(total,ans) # 비교하여 최댓값을 바꿔준다
    for i in range(n):
        if visited[i] == True: # 이미 작업한 숫자면
            continue # 다음 숫자로 진행한다.
        visited[i] = True # 해당 숫자를 방문처리 해준다.
        arr2.append(arr[i])# arr2에 삽입해준다
        dfs()# 다음 숫자를 넣기위해 재귀를 돌려준다.
        arr2.pop()# 가장 우측 숫자를 빼줘 새로운 배열을 만들 준비를 한다.
        visited[i] = False # 물론 방문처리도 취소해준다.

dfs()
print(ans)
