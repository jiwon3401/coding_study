import sys 
input = sys.stdin.readline 
from collections import deque
n,m = map(int, input().split())
Q = [(pos, val) for pos, val in enumerate(list(map(int, input().split())))] 
#index 까지 tuple로 
Q = deque(Q)
cnt = 0
while True: 
    cur = Q.popleft() #(0,60)
    if any(cur[1]<x[1] for x in Q): # x:위험도
        Q.append(cur)
    else: #cur이 위험도 젤 높을때
        cnt += 1
        if cur[0]==m:
            print(cnt)
            break
