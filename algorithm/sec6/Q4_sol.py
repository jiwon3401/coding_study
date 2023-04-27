
import sys
def DFS(L, sum): #L:인덱스번호
    if sum>total//2: #시간복잡도 줄이기 sum=total//2이라면 홀수때는 성립안되서 안됨 !
        return 
    if L==N:
        if sum== (total-sum): #다른 부분집합
            print("YES")
            sys.exit(0) #함수가 아니라 시스템 종료 !!
    else:
        DFS(L+1, sum+a[L])  # 부분집합 a[L]을 사용
        DFS(L+1, sum) #a[L] 사용x
    
if __name__ == "__main__":
    N = int(input())
    a = list(map(int, input().split()))
    total = sum(a)
    DFS(0,0)
    print("NO")