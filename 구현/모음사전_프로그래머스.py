def solution(word):
    letter = 'AEIOU'
    answer = 0
    count = 0
    
    def dfs(now, target):
        nonlocal count
        nonlocal answer
        
        if now == target:
            answer = count
            return

        if len(now) > 5:
            return

        count += 1

        for l in letter:
            dfs(now+l, target)
        
    dfs('', word)
    return answer