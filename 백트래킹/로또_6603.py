import sys
input = sys.stdin.readline


def dfs():
    if len(ans) == 6 and ans == sorted(ans):
        print(' '.join(map(str,ans)))
        return
    for i in range(len(lotto)):
        if visited[i]:
            continue
        visited[i] = True
        ans.append(lotto[i])
        dfs()
        ans.pop()
        visited[i] = False

while True:
    lotto = list(map(int,input().split()))
    if lotto[0] == 0:
        break
    visited=[False]*(lotto[0])
    ans = []
    del lotto[0]
    dfs()
    print()
    


    
