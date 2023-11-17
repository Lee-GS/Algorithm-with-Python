tc = int(input())

for i in range(1, tc+1):
    a,b = input().split()
    if a*3 in b*3 or b*3 in a*3:
        print(f'#{i} {"yes"}')
    else:
        print(f'#{i} {"no"}')
        