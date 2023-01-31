N = int(input())
array = list(map(int,input().split()))
M = int(input())
search = list(map(int,input().split()))

array.sort() # 입력받은 배열을 오름차순으로 정렬해준다.

def bst(array,target,start,end):
    if start>end: # 시작점이 끝점보다 클 경우
        return None
    mid = (start+end)//2
    if array[mid] == target: # 찾고자하는 수가 가운데있는 수와 같을 경우
        return array[mid]
    elif array[mid]>target: # 찾고자하는 수가 가운데있는 수보다 작을경우
        return bst(array,target,start,mid-1) # 가운데위치 보다 하나 아래 위치가 end가 되어 재귀로 실행
    else:
        return bst(array,target,mid+1,end) # 위와 반대로 가운데위치 보다 하나 위에 위치가 start가 되어 재귀로 실행
    
    
    
for i in range(M):
    if bst(array,search[i],0,len(array)-1) == None:
        print(0)
    else:
        print(1)
        
        