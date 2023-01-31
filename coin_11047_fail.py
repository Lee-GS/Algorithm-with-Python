import sys
n,k = map(int,sys.stdin.readline().split())
list = [0]*n
cnt = 0
arr = []
for i in range(n):
    list[i]=int(input()) 
j=0
while j < len(list):
    j=j+1
    if (list[j]>k):
        cnt = cnt + k//list[j-1]
        k=k%list[j-1]
        j=0
        if k == 0:
            break
    
    elif (list[j]==k):
        cnt=cnt+1
        break
    elif (k%list[j] == 0):
        arr.append(list[j])

if(k>list[n-1]):
        cnt=k/max(arr)
        
       
print(cnt)        
        
        