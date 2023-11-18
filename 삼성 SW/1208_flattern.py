
for tc in range(1,11):
    n = int(input())
    arr = list(map(int,input().split()))
    flag = False
    for i in range(n):
        a = max(arr)
        b = min(arr)
        x=arr.index(a)
        y=arr.index(b)
        arr[x] = arr[x] -1
        arr[y] = arr[y] +1
        if len(set(arr)) == 2 :
            flag = True
            print(f'{tc} {1}')
        elif len(set(arr)) == 1 :
            flag = True
            print(f'{tc} {0}')
    if flag==False:
        print(f'{tc} {max(arr)-min(arr)}')
            
        
            
        
    