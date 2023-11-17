for tc in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    total=0

    for i in range(2,len(arr)-2):
        tmp = [arr[i-2],arr[i-1],arr[i],arr[i+1],arr[i+2]]
        flag = 0
    
        for j in range(5):
            if j == 2:
                continue
            elif (arr[i]-tmp[j]) >=1:
                flag+=1
        else:
            if flag == 4:
                del tmp[2]
                total+=(arr[i]-max(tmp))
    print(f'#{tc} {total}')




