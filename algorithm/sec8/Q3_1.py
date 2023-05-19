#계단오르기(Top-Down : 메모이제이션)
'''
철수는 계단을 오를 때 한 번에 한 계단 또는 두 계단씩 올라간다. 만약 총 4계단을 오른다면
그 방법의 수는 1+1+1+1, 1+1+2, 1+2+1, 2+1+1, 2+2 로 5가지이다.
그렇다면 총 N계단일 때 철수가 올라갈 수 있는 방법의 수는 몇 가지인가?
'''
import sys
input = sys.stdin.readline

def DFS(v):
    if dp[v]>0:
        return dp[v]
    if v==1 or v==2:
        return v
    else: #dp[v]=dp[v-1]+dp[v-2]
        dp[v] = DFS(v-1)+DFS(v-2)
        return dp[v]
        
if __name__=="__main__":
    N= int(input())
    dp=[0]*(N+1)
    print(DFS(N))
    