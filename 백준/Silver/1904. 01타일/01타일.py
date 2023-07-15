import sys
input=sys.stdin.readline
N = int(input())
dy = [0]*(N+2)
dy[1]=1 
dy[2]=2 #00 11

for i in range(3,N+1):
    dy[i] = (dy[i-1]+dy[i-2])%15746
    
print(dy[N])