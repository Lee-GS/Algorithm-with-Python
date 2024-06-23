import sys
from itertools import combinations
import math
input = sys.stdin.readline

n = int(input())

gradient = []
answer = 10e9
for i in range(n):
    gradient.append(list(map(int,input().split())))

for i in range(1,len(gradient)+1):
    for j in combinations(gradient,i):
        shin = 1
        ssn = 0 
        for k in j:
            shin *=k[0]
            ssn+=k[1]
        #print(shin, ssn)
        answer = min(answer,abs(shin-ssn))

print(answer)



    