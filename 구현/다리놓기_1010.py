from itertools import combinations
import math
import sys
input = sys.stdin.readline

n = int(input())

for _ in range(n):
    a,b = map(int,input().split())
    print(math.comb(b,a))