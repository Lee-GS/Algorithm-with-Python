num = int(input())

list = []
list.append(0)
list.append(1)
i=2
if num == 0:
    print(0)
elif num == 1:
    print(1)
else:
    while i<num+1:
        list.append(list[i-1]+list[i-2])
        i+=1
    
print(list[num])    
