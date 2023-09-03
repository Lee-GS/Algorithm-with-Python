from itertools import permutations

def solution(k, dungeons):

    answer = -1
    hp = k
    for i in permutations(dungeons,len(dungeons)):
        cnt=0
        k = hp
        for j in range(len(dungeons)):
            if k >= i[j][0]:
                k-=i[j][1]
                cnt+=1
                answer = max(answer,cnt)
            else:
                break

    return answer
