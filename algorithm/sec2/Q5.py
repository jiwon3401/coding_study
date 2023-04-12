# [#5. 정다면체]
'''
두 개의 정 N면체와 정 M면체의 두 개의 주사위를 던져서 나올 수 있는 눈의 합 중 가장 확률이 높은 숫자를 출력하는 프로그램을 작성하세요.
정답이 여러 개일 경우 오름차순으로 출력합니다.
'''

import sys
input = sys.stdin.readline
N,M = map(int, input().split())
dict_sum = {}
for i in range(1,N+1):
    for j in range(1,M+1):
        ij_sum = i+j
        if ij_sum in dict_sum:
            dict_sum[ij_sum] +=1
        else:
            dict_sum[ij_sum] = 1
max_prob = [key for key, value in dict_sum.items() if max(dict_sum.values())==value]
print(*max_prob)


#sol
n,m = map(int, input().split())
cnt = [0] * (n+m+3) #(n+m)개
max = -2147000000
for i in range(1, n+1):
    for j in range(1, m+1):
        cnt[i+j] += 1
for i in range(n+m+1):
    if cnt[i] > max:
        max= cnt[i]
for i in range(n+m+1):
    if cnt[i] == max:
        print(i, end=' ')
        