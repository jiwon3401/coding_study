#[#10. 점수 계산]

import sys
input = sys.stdin.readline
N = int(input())
ans = list(map(int, input().split()))
cnt = 0
sum = 0
for i in ans:
    if i != 0:
        cnt += 1
        sum += cnt       
    else:
        cnt=0
print(sum)
