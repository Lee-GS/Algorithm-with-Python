import sys
input = sys.stdin.readline

n = int(input())
card1 = sorted(list(map(int,input().split())))
m = int(input())
card2 = list(map(int,input().split()))


dict = {} # 딕셔너리 선언

for i in card1:
    if i in dict: #값이 있을경우 +1을 해준다
        dict[i] +=1
    else: # 없을경우 새로 추가해준다
        dict[i]=1

def bst(array,target,start,end):
    if start>end:
        return 0
    mid = (start+end)//2
    if array[mid] == target: # 값을 찾을 경우 딕셔너리에서 해당 키의 밸류 값을 출력한다
        return dict.get(target)
    elif array[mid] >= target:
        return bst(array,target,start,mid-1)
    else:
        return bst(array,target,mid+1,end)

for i in card2:
    print(bst(card1,i,0,len(card1)-1), end=" ") # 정답 출력
    