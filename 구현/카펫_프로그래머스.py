
def solution(brown, yellow):
    answer = []
    arr = []
    total = brown+yellow
    
    for i in range(1,total+1):
        if total%i == 0: # 약수를 찾는다
            arr.append(i)

    if len(arr)%2 == 0: # 약수의 갯수가 짝수인 경우
        for i in range(len(arr)//2):# 가운데를 기준으로 인덱스를 한칸씩 줄이고 늘려나가야한다
            #brown과 갯수를 맞춰줘야 한다. 마지막에 -4를 해주는 이유는 겹치는 부분을 빼주는 것이다.
            if brown == (arr[len(arr)//2+i])*2+(arr[len(arr)//2-1-i]*2-4): 
                answer.append(arr[len(arr)//2+i]) # 큰값을 먼저 넣어준다
                answer.append(arr[len(arr)//2-1-i])
                break
    else: # 약수의 갯수가 홀수인 경우 아래 설명은 위와 동일
        for i in range(len(arr)//2+1):
            if brown == (arr[len(arr)//2+i])*2+(arr[len(arr)//2-i]*2-4): 
                answer.append(arr[len(arr)//2+i])
                answer.append(arr[len(arr)//2-i])
                break
        
    return answer