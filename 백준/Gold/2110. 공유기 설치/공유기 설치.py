import sys
input = sys.stdin.readline
N, C = map(int, input().split())
aa = []
for _ in range(N):
    aa.append(int(input()))

aa.sort()
start = 1
end = max(aa)-min(aa)
res = 0
while start<=end:
    mid = (start+end)//2
    cnt=1
    wifi=aa[0]

    for i in aa: #2번째부터
        if i >= wifi + mid:
            cnt += 1
            wifi = i
    
    if cnt >= C: #거리 넓히기
        res = mid
        start = mid+1

    else: #줄이기
        end = mid-1
        
print(res)



