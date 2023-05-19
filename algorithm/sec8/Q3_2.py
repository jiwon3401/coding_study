#돌다리 건너기(Bottom-Up)
'''
철수는 학교에 가는데 개울을 만났습니다. 개울은 N개의 돌로 다리를 만들어 놓았습니다. 철
수는 돌 다리를 건널 때 한 번에 한 칸 또는 두 칸씩 건너뛰면서 돌다리를 건널 수 있습니다.
철수가 개울을 건너는 방법은 몇 가지일까요?
'''
import sys
input = sys.stdin.readline 
N= int(input())
dp=[0]*(N+2)
dp[1]=1
dp[2]=2

for i in range(3,N+2):
    dp[i]=dp[i-1]+dp[i-2]
    
print(dp[N+1])
