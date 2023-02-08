import sys
input = sys.stdin.readline

n = int(input())
wine = [0]*(n+3)
dp = [0]*(n+3)

for i in range(1,n+1):
    wine[i]=int(input())

dp[1] = wine[1]
dp[2] = wine[1]+wine[2]
dp[3] = max(dp[2],wine[1]+wine[3],wine[2]+wine[3]) #3가지의 경우의 수를 먼저 대입해준다.

for i in range(4,n+1):
    dp[i] = max(dp[i-1],dp[i-2]+wine[i],dp[i-3]+wine[i-1]+wine[i]) # 각각의 경우의 수를 비교해가며 dp리스트를 채워준다.

print(dp[n]) # 해당 dp 출력