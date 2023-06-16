import math
def solution(numbers):
    answer = 0
    arr = list(numbers)
    visited = [False]*len(arr)
    ans = []
    def check(n):
        cnt=0
        if n == 1 or n == 0:
            return False
        # sqrt 함수를 사용하여 소수 검사의 범위를 줄여줘야 시간초과가 발생하지 않는다.
        # 해당 숫자의 제곱근의 이하의 수만 검사를 해줘도 그 수가 소수인지 아닌지 판별 할 수 있다.
        # 굳이 모든 숫자를 검사 해줄 필요가 없다!!
        for i in range(2,int(math.sqrt(n))+1): 
            if n%i == 0:
                cnt+=1
        if cnt == 0 :
            return True
        else:
            return False
    number=""
    def dfs(number):
        nonlocal answer        
        if number and check(int(number) or len(number) == len(arr)): 
            n = int(number)
            if n not in ans:
                ans.append(n)
        for i in range(len(arr)):
            if visited[i] == True:
                continue
            visited[i] = True
            number+=arr[i]
            dfs(number)
            number=number[:-1]
            visited[i] = False
            
            
    dfs(number)      
    answer = len(ans)
    return answer