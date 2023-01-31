num = int(input())
stair = list()
total = list()

for i in range(num):
    stair.append(int(input()))

total.append(stair[0])
total.append(max(stair[0]+stair[1] , stair[1]))
total.append(max(stair[0]+stair[2] , stair[1]+stair[2]))

for j in range(3, num):
    total.append(max(total[j-2]+stair[j] , total[j-3]+stair[j]+stair[j-1]))
        
print(total[-1])