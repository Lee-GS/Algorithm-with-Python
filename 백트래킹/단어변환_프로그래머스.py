def solution(begin, target, words):
    answer = 0
    ans = []
    visited=[False]*len(words)
    
    def check(before, after):  # 글자수가 1개만 다른지 검사하는 함수를 만들어준다.
        count = 0
        for i in range(len(before)):
            if before[i] == after[i]:
                count+=1
        if len(before)-count == 1: # 불일치하는 글자가 1개일 경우
            return True
        else:
            return False
        
    def dfs(cnt,word):
        if word == target: 
            ans.append(cnt)
            return 
        for i in range(len(words)):
            if check(word,words[i]):# 글자수 차이가 1개만 나오는지 확인한다.
                if visited[i]:# 방문 했을경우 그냥 넘어간다.
                    continue
                visited[i] = True
                dfs(cnt+1,words[i])# cnt를 늘려주며 몇회 걸리는지 세어준다.
                visited[i] = False
                
    if target not in words: # target이 words에 없을 경우
        return 0 # 0을 리턴한다.
    else:
        dfs(0,begin)
        answer = min(ans) # 최솟값을 찾아준다.
        
    
    return answer