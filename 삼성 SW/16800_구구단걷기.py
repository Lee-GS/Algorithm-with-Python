tc = int(input())

for a in range(1,tc+1):
    answer = []
    N = int(input())
    x=0
    y=0
    for i in range(1, int(N ** 0.5) + 1):
        if N % i == 0:
            answer.append(i)
            if i < N//i:
                answer.append(N//i)
	#answer.append(N)
    answer.sort()
    print(answer)
    if len(answer)%2 == 0:
        x = answer[len(answer)//2-1]-1
        y = answer[len(answer)//2]-1
        print(f'#{a} {x+y}')
    else:
        x = answer[len(answer)//2]-1
        y = answer[len(answer)//2]-1
        print(f'#{a} {x+y}')