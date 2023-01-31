x =int(input())
stick = [64,32,16,8,4,2,1]
cnt = 0

for i in range (len(stick)):
    if x >= stick[i]:
       cnt=cnt+1
       x=x-stick[i]
    elif x == 0:
        break  
print(cnt)