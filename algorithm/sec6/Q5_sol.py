import sys
from collections import deque
input = sys.stdin.readline 

def DFS(L,sum, tsum):
    global result
    if sum+(total-tsum)<result: # (total-tsum)=앞으로 판단해야 할 바둑이의 총 무게
        #더 최적이 답이 안나온다면 종료 -> 이렇게 해야 시간초과 안남 !!
        return
    if sum>c:
        return
    
    if L==n: #부분집합 말단노드
        if sum>result: #result를 참조
            result=sum #result를 재할당하면 local변수이므로 -> global 할당해줘야함
    else:
        DFS(L+1, sum+a[L], tsum+a[L]) #a의 L번째원소를 부분집합에 넣음.
        DFS(L+1, sum, tsum+a[L]) #a[L] 참여시키지 않겠다.
        #tsum-> 판단을 한 무게

if __name__=="__main__":
    c, n = map(int, input().split())
    a = [0]*n
    result=-2147000000
    for i in range(n):
        a[i] = int(input())
    total=sum(a)
    DFS(0,0,0) 
    print(result)