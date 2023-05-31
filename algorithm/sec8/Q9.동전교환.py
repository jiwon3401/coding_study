#동전교환(냅색 알고리즘)
'''
다음과 같이 여러 단위의 동전들이 주어져 있을때 거스름돈을 가장 적은 수의 동전으로 
교환 해주려면 어떻게 주면 되는가? 각 단위의 동전은 무한정 쓸 수 있다.
첫 번째 줄에는 동전의 종류개수 N(1<=N<=12)이 주어진다. 두 번째 줄에는 N개의 동전의 종류가 주어지고, 
그 다음줄에 거슬러 줄 금액 M(1<=M<=500)이 주어진다. 각 동전의 종류는 100원을 넘지 않는다.
'''

import sys 
input = sys.stdin.readline 
N = int(input())
coin = list(map(int, input().split()))
M = int(input())
dy = [1000]*(M+1) #dy[j]: j원을 거슬러주는데 필요한 동전 최소개수
# **최소문제를 구할때는 큰 값으로 초기화하는것**
dy[0]=0

for i in range(len(coin)):
    for j in range(coin[i], M+1):
        dy[j]= min(dy[j-coin[i]]+1, dy[j])
        
print(dy[M])
