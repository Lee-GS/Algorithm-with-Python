n = int(input())
price = list(map(int,input().split()))
dp = [0]*(n+1)

for i in range(1,n+1):
    tmp = []
    for j in range(1,i+1):
        dp[i] = price[j-1]+dp[i-j]
        tmp.append(dp[i])
    dp[i]=max(tmp)
print(dp[n])