import sys
input = sys.stdin.readline

n = int(input())
region = list(map(int,input().split()))
m = int(input())
ans = []

def bs(array,t,start,end):
    total = 0 # 값을 더해줄 total 변수
    if start > end:
        return None
    mid = (start+end)//2 # 상한선 구하기
    for i in array: # 배열에 있는 값을 상한선과 비교하여 더해줌
        if i >= mid: # 배열에 있는 값이 상한선이랑 같거나 크면
            total+=mid # 상한선을 더해준다
        else: #반대의 경우
            total+=i # 배열의 있는 값을 더해준다
    if(total<=t): # 다 더한값이 m의 값보다 작거나 같을때
        ans.append(mid) # 정답리스트에 추가
        return bs(array,t,mid+1,end) # 시작점을 상한선+1로 두고 재귀
    else:
        return bs(array,t,start,mid-1) #도착점을 상한선-1로 두고 재귀
    
bs(region,m,0,max(region))

print(max(ans)) #정답 리스트에서 최댓값 출력