import sys 
input=sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    
