
num =input()
a=len(num)
ans=0
for i in range (a):
    b=(int(num)-(10**i)+1)
    ans=ans+b
    
print(ans)
    