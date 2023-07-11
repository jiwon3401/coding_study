#[Q4.동전 바꿔주기(DFS)]
import sys
input = sys.stdin.readline

def DFS(L,sum):
    global cnt
    if sum>T:
        return
    
    if L==k and sum==T:
        cnt+=1
        
    elif L!=k:
        for i in range(n[L]+1): #동전 개수만큼 가지치기
            DFS(L+1, sum+p[L]*i)  #동전사용
            

if __name__=="__main__":
    T = int(input())
    k = int(input())
    p,n=[],[]
    cnt = 0
    
    for _ in range(k):
        a,b = map(int, input().split())
        p.append(a)
        n.append(b)
    
    DFS(0,0)
    print(cnt)