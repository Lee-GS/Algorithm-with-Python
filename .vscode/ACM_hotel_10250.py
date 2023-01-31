T=int(input())

for _ in range (T):
    h,w,n=map(int,input().split())
    
    if h>=n:
        print(n*100+1)
    else:
        a,b = divmod(n,h)
        if b == 0:
            print(100*h+a)
        else:
            print((100*b)+(a+1))
