#[Q8.순열구하기(DFS)]
'''
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 M개를 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
'''
import sys
input = sys.stdin.readline

def DFS(v):
    global cnt
    if v==M:
        print(*answer)
        cnt+=1
        #tmp[v]=0
    else:
        for i in range(1,N+1):
            if tmp[i]==0: #0일때만 가지 뻗어갈수있도록
                answer[v]=i
                tmp[i]=1
                DFS(v+1)  
                tmp[i]=0  #다시 back할때는 초기화
       
                        
if __name__=='__main__':
    N,M = list(map(int, input().split()))
    answer=[0]*M
    tmp=[0]*(N+1)
    cnt=0
    DFS(0)
    print(cnt)