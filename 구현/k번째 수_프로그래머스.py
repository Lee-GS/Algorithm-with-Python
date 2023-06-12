def solution(array, commands):
    answer = []
    for i in range(len(commands)):
        tmp = array[commands[i][0]-1:commands[i][1]] # 슬라이스 기능을 이용하여 풀면 간단하다.
        tmp.sort()
        answer.append(tmp[commands[i][2]-1])
        
    return answer