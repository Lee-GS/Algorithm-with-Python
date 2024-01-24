import sys
from collections import deque
input = sys.stdin.readline

def time_number(num):
    arr = deque(num)
    arr2 = []
    arr2.append(list(arr))
    for _ in range(3):
        arr.rotate(1)
        arr2.append(list(arr))
    num = min(arr2)
    num2 = ""
    for i in range(4):
        if num[i] == str(0):
            return 10000
        num2 += str(num[i])
    return int(num2)

tmp = time_number((''.join(input().split())))
cnt = 1
i = 1111
while(i<tmp):
    if time_number(str(i)) == i and time_number(str(i)) < tmp:
        cnt +=1
    i=i+1
print(cnt)




