#[#Q11.최대힙]

import sys
import heapq as hq
input = sys.stdin.readline 

heap=[]
while True:
    N = int(input())
    if N==0:
        if len(heap)==0:
            print(-1)
        else:
            print(-hq.heappop(heap))
    elif N==-1:
        break 

    else:
        hq.heappush(heap, -N)

