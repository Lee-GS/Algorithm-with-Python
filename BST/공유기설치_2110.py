n,c = map(int,input().split())
locate = []
for _ in range(n):
    locate.append(int(input()))
locate.sort()

ans = 0 
start = 1 # 집간 거리가 가장 짧은 1이므로 1로 잡는다
end = locate[-1]-locate[0] # 집간 거리가 가장 큰건 마지막값에 처음값을 뺀값이다. 

def bst(array,start,end,target):
    while start<=end:
        mid = (start+end)//2 #가장 짧은 거리와 가장 큰거리의 합을 2로 나눈것이 중간값이다.
        current = array[0] #현재위치는 첫번째 집으로 잡는다.
        count = 1 # 공유기가 첫번째 집에 설치가 됐기 때문에 1로 선언한다.

        for i in range(1,len(locate)): # 집들을 순서대로 검사한다.
            if locate[i] >= current+mid: #검사한 집이 current+mid(집간거리)보다 크거나 같으면 공유기를 설치 할 수 있기 때문에
                count+=1 # 공유기 카운트를 늘려주고
                current = array[i] # current를 방금 설치한 공유기 집으로 바꿔준다
        if count >= target: # 공유기의 개수가 c보다 크거나 같으면 
            global ans
            ans = mid # 정답에 현재 거리를 넣어주고 
            start=mid+1 # 공유기가 설치된 집간 거리를 늘려준다.
        else: 
            end = mid - 1# 반대로 집간 거리를 줄여준다.

bst(locate,start,end,c)
print(ans)

    