T = int(input())

for _ in range(T):  
    floor = int(input())
    room = int(input()) 
    
    apart = [x for x in range(1, room+1)] 
    print(apart)
    for k in range(floor):
        for i in range(1, room):
            apart[i] =apart[i]+apart[i-1]
    print(apart[-1])