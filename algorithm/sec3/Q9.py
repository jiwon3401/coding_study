#[#Q9. 곳감(모래시계)]
'''
지도 정보가 N*N 격자판에 주어집니다. 각 격자에는 그 지역의 높이가 쓰여있습니다. 
각 격자판의 숫자 중 자신의 상하좌우 숫자보다 큰 숫자는 봉우리 지역입니다. 봉우리 지역이 몇 개있는지 알아내는 프로그램을 작성하세요. 
격자의 가장자리는 0으로 초기화 되었다고 가정한다.
'''

import sys
input = sys.stdin.readline
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

#가장자리에 0 추가
m.insert(0, [0]*N) #첫번째 행에 추가
m.append([0]*N)    #마지막 행에 추가
for i in m:
    i.insert(0,0)
    i.append(0)

count = 0
for i in range(1,N+1):
    for j in range(1,N+1):
        #print(m[i][j])
        if m[i][j] <= m[i-1][j]: continue
        elif m[i][j] <= m[i+1][j]: continue
        elif m[i][j] <= m[i][j-1]: continue
        elif m[i][j] <= m[i][j+1]: continue
        else:
            count += 1

print(count)

    
