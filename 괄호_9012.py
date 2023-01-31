T=int(input())

for _ in range(T):
    cnt=0
    test=input()
    test2=list(test)
    
    for i in range(len(test2)):
        if test2[i] == "(":
            cnt=cnt+1
        else:
            cnt=cnt-1
        if cnt<0:
            print("NO")
            break                      
    if cnt == 0:
        print("YES")
    elif cnt>0:
        print("NO")                
    
    