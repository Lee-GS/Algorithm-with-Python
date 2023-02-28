N, K = map(int, input().split())

cnt = 0

nums = [True] * (N + 1) # 방문처리 해줄 리스트이다

for i in range(2, len(nums) + 1):
    for j in range(i, N+1, i): # i부터 n+1까지 i만큼 더해준다. 
        if nums[j] == True: # 미방문이면
            nums[j] = False # 방문처리 해준다.
            cnt = cnt + 1
            if cnt == K:
                print(j)
                break