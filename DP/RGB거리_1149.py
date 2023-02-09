n = int(input())
house = []
for _ in range(n):
    house.append(list(map(int,input().split())))

total = 0
ans = []
def dp(array,a,b):
    global total
    total += array[a][b]
    if a == 3:
        ans.append(total)
        return ans
    elif b == 0:
        if array[a+1][b+1]>=array[a+1][b+2]:
            dp(array,a+1,b+2)
        elif array[a+1][b+1]<=array[a+1][b+2]:
            dp(array,a+1,b+1)
    elif b == 1:
        if array[a+1][b-1]>=array[a+1][b+1]:
            dp(array,a+1,b+1)
        elif array[a+1][b-1]<=array[a+1][b+1]:
            dp(array,a+1,b-1)
    else:
        if array[a+1][b-2]>=array[a+1][b-1]:
            dp(array,a+1,b-1)
        elif array[a+1][b-2]<=array[a+1][b-1]:
            dp(array,a+1,b-2)
for i in range(3):
    dp(house,0,i)
