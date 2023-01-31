import math
num = list(map(int,input()))
dup_list = []

for i in range(10):
    cnt = num.count(i)
    dup_list.append(cnt)
    print(dup_list)
    
if max(dup_list) in dup_list[0:6] or max(dup_list) in dup_list[7:9]:
    print (max(dup_list))
    
elif dup_list[6] == max(dup_list) or dup_list[9] == max(dup_list):
    max=(dup_list[6] + dup_list[9])/2
    max=math.ceil(max)
    print(max) 