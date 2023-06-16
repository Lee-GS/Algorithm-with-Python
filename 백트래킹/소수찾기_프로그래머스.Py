
def solution(numbers):
    answer = 0
    arr = list(numbers)
    visited = [False]*len(arr)
    
    def check(number):
        if number == 1 or number == 0:
            return False
        for i in range(1,number+1):
            if number%i == 0:
                cnt+=1
        if cnt == 2:
            return True
        else:
            return False
    number=""
    def dfs(number):
        nonlocal answer
        if check() or number == len(arr):
            answer+=1
        for i in range(len(arr)):
            if visited[i] == True:
                return
            visited[i] = True
            number+=arr[i]
            dfs(number)
            number-=arr[i]
            visited[i] = False
            
    dfs(number)      
            
    return answer