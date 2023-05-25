#최대 선 연결하기(LIS 응용)
'''
왼쪽의 번호와 오른쪽의 번호가 있는 그림에서 같은 번호끼리 선으로 연결하려고 합니다.
왼쪽번호는 무조건 위에서부터 차례로 1부터 N까지 오름차순으로 나열되어 있습니다.
오른쪽의 번호 정보가 위부터 아래 순서로 주어지만 서로 선이 겹치지 않고 최대 몇 개의 선을 
연결할 수 있는 지 구하는 프로그램을 작성하세요.
'''
import sys 
input = sys.stdin.readline 
N= int(input())
num = list(map(int, input().split()))
num.insert(0,0) 

dy = [0]*(N+1)
dy[1]=1
MAX=0

for i in range(2,N+1):
    max=0
    for j in range(i-1,0,-1):
        if num[i]>num[j] and dy[j]>max:
            max=dy[j]
        dy[i]=max+1 #이전에 구한 max값에 자기자신 +1
        
        if dy[i]>MAX:
            MAX = dy[i]
print(MAX)
