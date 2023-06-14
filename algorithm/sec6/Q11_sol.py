import sys
input = sys.stdin.readline

def DFS(L, s, sum): 
    global cnt
    if L==k: #k개를 다 뽑으면
        if sum%m==0:
            cnt+=1
    else:
        for i in range(s,n): # 0 ~ n-1
            DFS(L+1,i+1,sum+a[i])
            
    
if __name__=="__main__":
    n,k = map(int, input().split())
    a=list(map(int, input().split()))
    m=int(input())
    cnt=0
    DFS(0,0,0)
    print(cnt)