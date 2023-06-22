import sys
input = sys.stdin.readline

n,m = map(int,input().split())
answer = 0
square = []

for _ in range(n):
    square.append(list(input()))

short = min(n,m) #가장 작은변의 길이가 정사각형의 최대 크기가 됨으로 가장 작은변을 찾아준다

for k in range(short):
    for i in range(n-k):# k 값이 변해짐에따라 비교할 수 있는 범위도 달라짐으로 -k를 해주어야 한다.
        for j in range(m-k):
            if square[i][j] == square[i][j+k] and square[i][j] == square[i+k][j+k] and square[i][j] == square[i+k][j]: # 4 꼭짓점의 일치 여부 확인
                answer = max(answer,((k+1)**2))
            
print(answer)
