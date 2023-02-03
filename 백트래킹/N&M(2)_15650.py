import sys
input = sys.stdin.readline

n,m = map(int,input().split())
ans = []
visited = [False]*(n+1)

def dfs():
    if len(ans) == m: # 조건처럼 리스트의 길이가 m이 되면 출력해준다
        a = sorted(ans) # ans를 오름차순으로 정렬시킨 후 a에 저장
        if ans == a: # 오름차순으로 정렬된 a와 ans가 같은 경우에만 출력해준다.
            print(' '.join(map(str,ans)))
            return
    for i in range(1,n+1):
        if visited[i] == True: # 방문했을경우 continue 해준다
            continue
        visited[i] = True # 미방문일경우 방문처리를 해준다
        ans.append(i) # 그리고 리스트에 추가해준다
        dfs() # 이어서 dfs문을 재귀함수로 실행한다
        ans.pop() # 마지막에 추가됐던 수를 빼준다.
        visited[i] = False # 여기가 중요!!!! 방문했던곳을 다시 미방문 처리 해준다
        
        
dfs()