from itertools import permutations, combinations
n,k = map(int,input().split())

arr = list(range(1,n+1))
combi = list(combinations(arr,k))

print(len(combi))
