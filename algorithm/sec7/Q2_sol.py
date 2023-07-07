import sys
input = sys.stdin.readline

def DFS(L,sum):
    global res
    if L==n+1:
        if sum>res: #갱신
            res = sum
    else:
        if L+T[L]<=n+1: #현재날짜 L + 상담 걸리는 기간
            DFS(L+T[L], sum+P[L]) #L이라는 날짜에 상담을 했을 때
        
        DFS(L+1, sum)  #상담하지 않는 경우 -> 1씩 증가하다보면 n+1로 가게 됨
    
    
if __name__=="__main__":
    n = int(input())
    T = list()
    P = list()
    for _ in range(n):
        a,b = map(int, input().split())
        T.append(a)
        P.append(b)
    res = -21400000
    T.insert(0,0)
    P.insert(0,0)
    
    DFS(1,0)
    print(res)