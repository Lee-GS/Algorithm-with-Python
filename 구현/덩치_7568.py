n = int(input())
 
physical = []
ans = [] 
for i in range(n):
    a, b = map(int, input().split())
    physical.append((a, b)) 
 
for i in range(n):
    count = 0
    for j in range(n):
        if physical[i][0] < physical[j][0] and physical[i][1] < physical[j][1]: 
            count += 1 
    ans.append(count + 1) 
 
for i in ans:
    print(i,end=" ")