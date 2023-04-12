import sys
input = sys.stdin.readline
N,M = map(int, input().split())
nums = list(map(int, input().split()))
nums.sort()
p = 0
q = N-1

for i in range(N): #while p<=q:
    mid = (p+q)//2
    if nums[mid] == M:
        print(mid+1)
        break
    elif nums[mid] > M:
        q = mid-1
    else:
        p = mid+1