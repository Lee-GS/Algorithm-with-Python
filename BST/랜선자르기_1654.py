import sys
input = sys.stdin.readline

k,n = map(int,input().split())
line = [] # 전선을 입력 받을 리스트
ans = [] # 11개가 맞아 떨어지는 정답들을 넣을 리스트
for i in range(k):
    line.append(int(input())) 


def BS(array,t,start,end):
    total = 0 # n과 비교할 total변수다
    if start>end:
        return None
    mid = (start+end)//2
    for i in array:
        total += i//mid # 각각의 전선들과 나눠주면서 몫을 더해준다
        
    if total >= t: # 그렇게 더한 몫이 t와 같거나 크면  
        ans.append(mid) # 정답 리스트에 넣어준다
        return BS(array,n,mid+1,end) # 그리고 다시 재귀를 돌려준다 
    else:
        return BS(array,n,start,mid-1) # total이 t보다 작을 경우 범위를 수정해 재귀를 돌려준다
    
BS(line,n,1,max(line)) # start가 0이 아닌 1부터 시작하는 이유는 선이 0m일 수는 없기 때문이다

print(max(ans)) # 최댓값을 출력해준다.

        