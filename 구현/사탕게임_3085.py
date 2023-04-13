import sys
input = sys.stdin.readline

n = int(input())
candyList = [list(input()) for _ in range(n)]
maxCandy = 0

def check():
    global maxCandy
    for i in range(n):
        cnt = 1
        #행 탐색
        for j in range(1,n):
            if candyList[i][j] == candyList[i][j-1]: # 행으로 연속되는 요소가 있을경우
                cnt+=1
                maxCandy = max(cnt,maxCandy)
            else:
                cnt=1
           
        cnt=1
        #열 탐색
        for j in range(1,n):
            if candyList[j][i] == candyList[j-1][i]:# 열로 연속되는 경우가 있을경우
                cnt+=1
                maxCandy = max(cnt,maxCandy)
            else:
                cnt = 1
            
        

for i in range(n):
    for j in range(n):
        if j+1 < n:
            #오른쪽꺼와 변겅
            candyList[i][j], candyList[i][j+1] = candyList[i][j+1], candyList[i][j]
            #검사
            check()
            # 원위치 시킨다
            candyList[i][j], candyList[i][j+1] = candyList[i][j+1], candyList[i][j] 
        
        if i+1 < n:
            #아래쪽꺼와 변경
            candyList[i][j], candyList[i+1][j] = candyList[i+1][j], candyList[i][j]
            #검사
            check()
            #원위치 시킨다
            candyList[i][j], candyList[i+1][j] = candyList[i+1][j], candyList[i][j] 

print(maxCandy)
