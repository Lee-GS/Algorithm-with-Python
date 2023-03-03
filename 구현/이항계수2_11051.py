import math

n,k = map(int,input().split())

print(math.comb(n,k)%10007)