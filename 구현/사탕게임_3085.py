import sys
input = sys.stdin.readline

n = int(input())
candyList = [list(input()) for _ in range(n)]
maxCandy = 0

def check():
    global maxCandy
    for i in range(n):
        cnt = 1
        for j in range(1,n):
            if candyList[i][j] == candyList[i][j-1]:
                cnt+=1
                maxCandy = max(cnt,maxCandy)
            else:
                cnt=1
           
        cnt=1
        for j in range(1,n):
            if candyList[j][i] == candyList[j-1][i]:
                cnt+=1
                maxCandy = max(cnt,maxCandy)
            else:
                cnt = 1
            
        

for i in range(n):
    for j in range(n):
        if j+1 < n:
            candyList[i][j], candyList[i][j+1] = candyList[i][j+1], candyList[i][j]
            check()
            candyList[i][j], candyList[i][j+1] = candyList[i][j+1], candyList[i][j] 
        
        if i+1 < n:
            candyList[i][j], candyList[i+1][j] = candyList[i+1][j], candyList[i][j]
            check()
            candyList[i][j], candyList[i+1][j] = candyList[i+1][j], candyList[i][j] 

print(maxCandy)
