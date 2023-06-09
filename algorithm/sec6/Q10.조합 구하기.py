#[Q10.조합 구하기(DFS)]


import sys
input = sys.stdin.readline

def DFS(L,S):
    global cnt
    
    
    if L==M:
        print(*answer)
        cnt+= 1
    
    else:
        for i in range(S,N+1):
            answer[L]=i
            
            DFS(L+1, i+1)
            
    
if __name__=="__main__":
    N,M = list(map(int, input().split()))
    answer=[0]*M
    cnt=0
    DFS(0,1)
    print(cnt)
    