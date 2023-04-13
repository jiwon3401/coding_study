#[Q3.부분집합 구하기(DFS)]
'''
자연수 N이 주어지면 1부터 N까지의 원소를 갖는 집합의 부분집합을 모두 출력하는 프로그램
을 작성하세요.

상태트리

'''
import sys 

def DFS(v): #
    if v == N+1: #종착점 4->종료
        for i in range(1,N+1):
            if ch[i]==1: #인덱스를 찍어야하므로
                print(i, end=' ')
        print()
    
    else:
        ch[v] = 1 #부분집합으로 사용
        DFS(v+1)
        ch[v] = 0 #사용x
        DFS(v+1)
    

if __name__ == "__main__":
    N = int(input())
    ch = [0]*(N+1) #체크박스
    DFS(1) 