#[1. K번째 약수풀이]

import sys
input = sys.stdin.readline
N, K = map(int, input().split())
div = []
try:
    for i in range(1,N+1):
        if N%i == 0:
            div.append(i)
    print(div[K-1])
except:
    print(-1)


##sol
n, k = map(int, input().split())
cnt = 0
for i in range(1,n+1):
    if n%i == 0:
        cnt +=1
    if cnt == k:
        print(i)
        break
else:
    print(-1)