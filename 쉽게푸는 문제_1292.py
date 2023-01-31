a,b = map(int,input().split())
list = []

for i in range(1,1001):
    for k in range(i):
        list.append(i)
     
sum = 0 

for i in range(a-1,b):
    sum+=list[i]        

print(sum)    