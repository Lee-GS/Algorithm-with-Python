import sys 
list_A = []
list_B = []
list_C = []

for _ in range (4):
    a,b=map(int,sys.stdin.readline().split())
    list_A.append(a)
    list_B.append(b)

list_C.append(list_B[0])

for i in range (3):
    count = list_C[i]-list_A[i+1]+list_B[i+1]
    list_C.append(count)

print(max(list_C))
    