'''
N개의 정수가 주어지면 그 숫자들 중 K개를 뽑는 조합의 합이 임의의 정수 M의 배수인 개수는 몇 개가 있는지 출력하는 프로그램을 작성하세요.
예를 들면 5개의 숫자 2 4 5 8 12가 주어지고, 3개를 뽑은 조합의 합이 6의 배수인 조합을 찾으면 4+8+12 2+4+12로 2가지가 있습니다.
'''

import sys
input = sys.stdin.readline

def DFS(L,S):
    global cnt
    if L==K:
        if sum(answer)%M==0:
            cnt+=1
        
    else:    
        for i in range(S,N+1):
            answer[L]=i 
            DFS(L+1, i+1)
    

if __name__=="__main__":
    N, K = list(map(int, input().split()))
    nums = list(map(int, input().split()))
    answer=[0]*K
    cnt=0
    M = int(input())
    DFS(0,1)
    print(cnt)
    