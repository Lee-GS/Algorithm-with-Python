import math
import sys
input = sys.stdin.readline

n = int(input())
infi = int(10e9) # 무한대를 설정해준다.

def prime_number(m): # 소수판별 함수 에라토스테네스의 체를 이용한다.
    if m == 1 or m == 0:
        return False
    for i in range(2,int(math.sqrt(m))+1): 
        if m%i == 0:
            return False
    return True
    
def pelindrom(m): # 펠린드롬수 판별 함수이다.
    m = str(m)
    if m == m[::-1]:
        return True
    else:
        return False

for i in range(n,infi): # n 부터 무한대까지 검사를 하다가 숫자를 발견하면 출력해주고 종료!!
    if prime_number(i) and pelindrom(i):
        print(i)
        break
