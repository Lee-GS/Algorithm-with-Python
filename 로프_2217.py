n = int(input())
rope = []
for _ in range(n):
    rope.append(int(input()))
rope.sort()    
rope_length = len(rope)
max_weight = []
cnt=0
for _ in range(rope_length):
    rope_length2 = len(rope)
    print(rope)
    if rope[rope_length2-1] != rope[rope_length2-2]:
        a=rope.pop()
        max_weight.append(a*cnt)
        print(a)
        print(max_weight)
    elif rope_length2 == 1:
        max_weight.append(rope[0]*cnt)
        break
    else:
        rope.pop()
    cnt+=1
print(max(max_weight))