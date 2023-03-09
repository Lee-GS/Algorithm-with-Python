from itertools import combinations_with_replacement

n  = int(input())

arr = list(combinations_with_replacement(range(4),n))
print(len(arr))
