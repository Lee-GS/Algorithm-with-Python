def solution(numbers, target):
    answer = 0
    
    def dfs(idx,total):
        nonlocal answer
        if idx == len(numbers): # 종료조건
            if total == target:
                answer+=1
            return
        else:
            dfs(idx+1,total+numbers[idx]) #더했을경우
            dfs(idx+1,total-numbers[idx]) #뺏을경우
            
    dfs(0,0)
    return answer