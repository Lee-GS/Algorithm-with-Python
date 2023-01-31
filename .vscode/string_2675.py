T = int(input())

for _ in range(T):
    n,str = input().split()
    n=int(n)
    
    new_str=list(str)
    
    str1=new_str[0]*n
    for i in range (1,len(new_str)):
        str1+=new_str[i]*n
    print(str1)        
    