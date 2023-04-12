'''
김진영이 듣도 못한 사람의 명단과, 보도 못한 사람의 명단이 주어질 때, 듣도 보도 못한 사람의 명단을 구하는 프로그램을 작성하시오.
'''

N, M = map(int,input().split())
N_list = []
M_list = []
for _ in range(N):
    a = input()
    N_list.append(a)
    
for _ in range(M):
    b = input()
    M_list.append(b)

NM_list = sorted(list(set(N_list)&set(M_list)))

print(len(NM_list))
for i in NM_list:
    print(i)
