from collections import deque
def solution(progresses, speeds):
    answer = []
    progresses1 = deque(progresses)
    cnt=0
    while progresses1:
        for i in range(len(progresses1)):
            progresses1[i]+=speeds[i]
            
        while progresses1 and progresses1[0] >=100:
            progresses1.popleft()
            speeds.pop(0)
            cnt+=1
            
        if cnt != 0:
            answer.append(cnt)
            cnt = 0
        
                
    return answer