#[Q9.순열추측하기(순열,파스칼 응용)]
'''
가장 윗줄에 1부터 N까지의 숫자가 한 개씩 적혀 있다. 그리고 둘째 줄부터 차례대로 파스칼 의 삼각형처럼 위의 두개를 더한 값이 저장되게 된다.
N과 가장 밑에 있는 숫자가 주어져 있을 때 가장 윗줄에 있는 숫자를 구하는 프로그램을 작성하시오. 
단, 답이 여러가지가 나오는 경우에는 사전순으로 가장 앞에 오는 것을 출력하여야 한다.
'''
import sys
input=sys.stdin.readline

def DFS(L, sum):
    if L==N and sum == F:
        for i in permut:
            print(i, end=' ')
        
        sys.exit(0) #처음 발견된 것만 실행시키고 프로그램 종료
        
    else:
        for i in range(1,N+1):
            if ch[i]==0:
                ch[i]=1 #이미 사용
                permut[L]=i #순열
                DFS(L+1, sum+ (permut[L]*binary[L])) #p*n을 더해서 F가 나오면 끝.
                ch[i]=0

if __name__=="__main__":
    N,F = map(int, input().split())
    binary = [1]*N #이항계수
    permut = [0]*N #순열
    ch = [0]*(N+1) 
    
    for i in range(1,N):
        binary[i]=binary[i-1]*(N-i)/i
    
    DFS(0,0)
        