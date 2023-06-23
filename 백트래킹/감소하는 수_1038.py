from itertools import combinations
import sys
input = sys.stdin.readline

n = int(input())

result = []
for i in range(1, 11):# 1자리 부터 10의자리까지 해준다
	for j in combinations(range(10), i): # 모든 경우의 수를 찾아낸다 
		num = ''.join(list(map(str, reversed(list(j))))) # 공백없는 문자열로 바꾸어준다.
		result.append(int(num)) # 숫자로 바꾸어 리스트에 삽입!

result.sort()

if n >= len(result):
	print(-1)
else:
	print(result[n])

