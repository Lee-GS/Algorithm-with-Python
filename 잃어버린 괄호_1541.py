s = list(input().split('-')) # '-'으로 구분한 리스트를 입력받는다
#예제 1의 경우 s = [55,50+40] 으로 받아진다.
res = 0
nums = []
for i in s:
    num = i.split("+")
    x = 0
    for j in num:
        x += int(j)
    nums.append(x) # 위의 과정을 거치면 nums = [55,90] 으로 선언된다
res = nums[0]

for i in range(1,len(nums)): # nums의 길이에서 1을 뺀 값이 - 의 갯수가 되므로 범위를 이와같이 설정해준다.
    res -= nums[i]

print(res)
