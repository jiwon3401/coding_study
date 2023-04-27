#[Q4. 합이 같은 부분집합(DFS)]
'''
N개의 원소로 구성된 자연수 집합이 주어지면, 이 집합을 두 개의 부분집합으로 나누었을 때 
두 부분집합의 원소의 합이 서로 같은 경우가 존재하면 “YES"를 출력하고, 그렇지 않으면 ”NO"를 출력하는 프로그램을 작성하세요.
둘로 나뉘는 두 부분집합은 서로소 집합이며, 두 부분집합을 합하면 입력으로 주어진 원래의 집합이 되어 합니다.
'''
import sys

def dfs(V):
    if V==n:
        sum=0
        for i in range(n):
            if check[i]==1: #인덱스 찍기
                sum += aa[i]
        if sum==(total-sum):
            print("YES")
            sys.exit(0)
        if sum>total//2: #시간복잡도 줄이기.
            return
    else:
        check[V]=1 #사용o
        dfs(V+1)
        check[V]=0 #사용x
        dfs(V+1)

if __name__=='__main__':
    n = int(input())
    aa = list(map(int, input().split()))
    check=[0]*n #체크리스트
    total = sum(aa)
    dfs(0) 
    print("NO") 
    #재귀함수 돌고 total-sum!=sum 이어서 main으로 돌아와서 "no" 출력
