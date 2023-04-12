#[#Q4. 두 리스트 합치기]
'''
오름차순으로 정렬이 된 두 리스트가 주어지면 두 리스트를 오름차순으로 합쳐 출력하는 프로그램을 작성하세요.
'''
import sys
input = sys.stdin.readline
N = int(input())
N_list = list(map(int, input().split()))
M = int(input())
M_list = list(map(int, input().split()))

sum_list = N_list + M_list 

for i in range(len(sum_list)-1):
    for j in range(len(sum_list)-i-1):
        if sum_list[j] > sum_list[j+1]:
            sum_list[j], sum_list[j+1] = sum_list[j+1], sum_list[j]

#print(*sum_list)
print(" ".join([str(i) for i in sum_list]))

