import sys
input = sys.stdin.readline

num = int(input())
dp=[0]*(num+3)
d=[0]*(num+3)

for i in range (1,num+1):
    d[i]=int(input())

dp[1]=d[1]
dp[2]=d[1]+d[2]
dp[3]=max(d[3]+d[2],d[1]+d[3])
    

for j in range(4,num+1):
    dp[j]=max(dp[j-3]+d[j]+d[j-1],dp[j-2]+d[j])

print(dp[num])        