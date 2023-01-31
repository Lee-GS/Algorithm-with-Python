import sys
input = sys.stdin.readline

n,m = map(int,input().split())
array = list(map(int,input().split()))
array.sort() # 이분탐색은 정렬이 기본이다.
answer = [] # 적어도 m미터를 절단할수 있는 절단기의 높이들을 담을 리스트

def bst(array,m,start,end):
    total = 0
    if start>end:
        return None
    mid = (start+end)//2
    for i in range(len(array)): # 각각의 나무들에 대해 비교를 해줘야한다
        tmp=array[i]-mid #나무의 높이에 절단기의 높이를 뺀다
        if tmp>=0: # 잘랐을때의 나무의 길이가 0보다 크거나 같으면
            total+=tmp # total에 더해준다
    if total >= m: # total이 m보다 크거나 같을경우 조건에 부합하기 때문에
        answer.append(mid) # answer 리스트에 넣어준다
        return bst(array,m,mid+1,end) # 그리고 조건에 부합했던 절단기의 높이를 start로 삼아 재귀를 돌려 또 이분탐색을 해준다
    else:
        return bst(array,m,start,mid-1)

bst(array,m,0,array[-1])
print(max(answer)) # 조건에 부합하는 요소들중에 최댓값을 출력한다.