import sys
input = sys.stdin.readline

n = int(input())
m = int(input())
s = input()

index = 0
cnt = 0
result = 0

while index < m-1: # 문자열의 길이보다 1개 낮게 검사한다.
    if s[index:index + 3] == 'IOI': # 3개의 연속되는 문자열이 "IOI"와 같을때!! 
        cnt += 1
        index += 2 # 마지막의 I 부터 다시 세야함으로 +2를 해준다.
        if cnt == n: # IOI의 갯수가 n과 같다면
            result += 1 # 정답을 하나 늘려준다.
            cnt -= 1 
    else: # 같은 문자열이 없다면 
        index += 1 # 다음 문자열부터 검사하게 한다.
        cnt = 0

print(result)

