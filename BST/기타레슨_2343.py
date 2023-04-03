import sys
input = sys.stdin.readline
n,m = map(int,input().split())
lecture = list(map(int,input().split()))
total =  sum(lecture)
result = 10**9
start = max(lecture)
end = total

while start<=end:
    mid = (start+end)//2
    cnt = 1
    tmp = 0

    for i in range(n):
        if(tmp+lecture[i] <= mid):
            tmp+=lecture[i]
        else:
            cnt+=1
            tmp = lecture[i]
        if cnt > m:
            break
    if cnt > m:
        start = mid + 1
    else:
        end = mid - 1 
        if (mid >= max(lecture)):
            result = min(result,mid)
print(result)
        