def solution(answers):
    answer = []
    first = [1,2,3,4,5]*2000
    second = [2,1,2,3,2,4,2,5]*1250
    third = [3,3,1,1,2,2,4,4,5,5]*1000
    n = len(answers)
    ans = []
    
    def check(arr):
        cnt = 0
        for i in range(n):
            if arr[i] == answers[i]: # 해당 리스트에 쭉 비교해준다.
                cnt+=1
        return cnt
    
    ans.append(check(first))
    ans.append(check(second))
    ans.append(check(third))

    m = max(ans)
    
    for i in range(len(ans)):
        if ans[i] == m: # 최댓값과 동일한 리스트는
            answer.append(i+1) # 정답 리스트에 넣어준다.
    
        
    return answer