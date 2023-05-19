#네트워크 선 자르기(Bottom-Up)
'''
현수는 네트워크 선을 1m, 2m의 길이를 갖는 선으로 자르려고 합니다.
네트워크 선의 길이가 Nm라면 몇 가지의 자르는 방법을 생각할 수 있나요?
첫째 줄은 네트워크 선의 총 길이인 자연수 N(3≤N≤45)이 주어집니다.
첫 번째 줄에 부분증가수열의 최대 길이를 출력한다.
'''
import sys 
input = sys.stdin.readline
N=int(input())
dy=[0]*(N+1)
dy[0]=1
dy[1]=2
for i in range(2,N):
    dy[i]=dy[i-1]+dy[i-2]
print(dy[N-1])


##sol
n=7
dy=[0]*(n+1)
dy[1]=1
dy[2]=2
for i in range(3,n+1):
    dy[i]=dy[i-1]+dy[i-2]
print(dy[n])
