def solution(tickets):
    answer = []
    ans = ["ICN"]
    visited = [False]*len(tickets)
    
    def dfs(nation):
        if len(ans) == (len(tickets)+1):
            tmp = ans[:] # 그대로 집어 넣으면 얕은복사 오류가 발생함으로 깊은복사로 바꿔주고 넣어준다.
            answer.append(tmp)
            return
        for i in range(len(tickets)):
            if tickets[i][0] == nation:
                if visited[i]:
                    continue
                visited[i] = True
                ans.append(tickets[i][1])
                dfs(tickets[i][1])
                ans.pop()
                visited[i] = False
                
    dfs("ICN")
    answer.sort() # 방법이 여러개일경우 알파벳 순으로 정렬을 해야한다
    answer = answer[0]# 첫번째 리스트가 알파벳 순으로 먼저 오는 리스트이다.
    
    return answer