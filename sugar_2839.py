import sys
N = int(sys.stdin.readline())
cnt =0
dp = []
for i in range(N):
    num3=3*i
    num=N-num3
    if(N==3 or N==5):
        dp.append(1)
        break
    if(N==4 or N==7):
        dp.append(-1)
        break
    if(num<0):
        break
    if(num%5==0):
        num5=num//5
        cnt=i+num5
        dp.append(cnt)
print(min(dp))

