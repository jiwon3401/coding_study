import sys
import heapq as hq
input=sys.stdin.readline
N= int(input())

hh = []
for _ in range(N):
    x= int(input())
    if x==0:
        if len(hh)==0:
            print(0)
        else:
            print(hq.heappop(hh))
    else:
        hq.heappush(hh,x)