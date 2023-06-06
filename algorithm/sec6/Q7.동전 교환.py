#동전교환-Cut Edge Tech
'''
1부터 N까지 번호가 적힌 구슬이 있습니다. 이 중 중복을 허락하여 M번을 뽑아 일렬로 나열하는 방법을 모두 출력합니다.
'''
#동전종류만큼 가닥을 뻗음
import sys
input=sys.stdin.readline

def DFS(L,total):
    global answer
    if L>total: #cut edge
        return
    if total>M:
        return
    if total==M:
        if L<answer: #참조
            answer=L #answer -> 지역변수로 인식하므로 global 선언
    else:
        for i in range(N): 
            '''D(0,0) -> D(1,5) -> D(2,10) -> D(3,15) ..
            '''
            DFS(L+1, coin[i]+total) #coin
        
    
if __name__=="__main__":
    N=int(input())
    coin=list(map(int,input().split()))
    M=int(input())
    answer=11111111111 #최소개수
    coin.sort(reverse=True)
    DFS(0,0)
    print(answer)