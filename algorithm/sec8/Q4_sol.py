import sys 
input=sys.stdin.readline

n = int(input())
arr = list(map(int, input().split()))
arr.insert(0,0)
dy=[0]*(n+1)
dy[1]=1
res=0
for i in range(2,n+1):
    max=0
    for j in range(i-1,0,-1):
        if arr[j]<arr[i] and dy[j]>max: #dy[j]: arr[j]가 마지막 항일 때 최대 수열 길이를 의미
            max=dy[j]
    dy[i]=max+1
    if dy[i]>res: #최대값 찾기
        res=dy[i]
print(res)