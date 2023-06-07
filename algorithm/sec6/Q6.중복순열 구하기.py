#[Q6.중복순열 구하기(DFS)]
'''
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
'''

import sys
input = sys.stdin.readline

def DFS(v):
    global cnt
    if v==M:
        print(*answer)
        cnt+=1
        
        '''
    if v==M:
        for j in range(M):
            print(answer[j], end=' ')
    '''
    else:
        for i in range(1,N+1):
            answer[v]=i
            DFS(v+1)


if __name__=="__main__":
    N,M = list(map(int, input().split()))
    answer=[0]*M
    cnt=0
    DFS(0)
    print(cnt)
    