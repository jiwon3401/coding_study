#[#5. 수들의 합]
'''
N개의 수로 된 수열 A[1], A[2], …, A[N] 이 있다. 이 수열의 i번째 수부터 j번째 수까지의
합 A[i]+A[i+1]+…+A[j-1]+A[j]가 M이 되는 경우의 수를 구하는 프로그램을 작성하시오.
'''
import sys
input = sys.stdin.readline
N, M = map(int, input().split())
seq = list(map(int, input().split()))

cnt = 0
for i in range(N+1):
    for j in range(i+1, N+1):
        if sum(seq[i:j]) == M:
            cnt += 1
print(cnt)
