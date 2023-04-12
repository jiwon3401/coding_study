#[#7. 소수(에라토스테네스 체)]
'''
자연수 N이 입력되면 1부터 N까지의 소수의 개수를 출력하는 프로그램을 작성하세요.
제한시간 1초
'''
import sys
input = sys.stdin.readline()
N = int(input())
count_list = [0]*(N+1)
cnt = 0 #소수 개수 카운트
for i in range(2,N+1): #1은 제외
    if count_list[i] == 0:
        cnt += 1
        for j in range(i, N+1):
            if j%i == 0:
                count_list[j] = 1
print(cnt)               
        
            
#sol
n = int(input())
ch = [0] * (n+1)
cnt = 0
for i in range(2, n+1):
    if ch[i] == 0:
        cnt+=1
        for j in range(i, n+1, i):
            ch[j] = 1
print(cnt)
