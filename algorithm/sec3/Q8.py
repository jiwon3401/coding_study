'''
현수는 곳감을 만들기 위해 감을 깍아 마당에 말리고 있습니다. 현수의 마당은 N*N 격자판으로 이루어져 있으며, 
현수는 각 격자단위로 말리는 감의 수를 정합니다. 그런데 해의 위치에 따라 특정위치의 감은 잘 마르지 않습니다. 
그래서 현수는 격자의 행을 기준으로 왼쪽, 또는 오른쪽으로 회전시켜 위치를 변경해 모든 감이 잘 마르게 합니다.
만약 회전명령 정보가 2 0 3이면 2번째 행을 왼쪽으로 3만큼 아래 그림처럼 회전시키는 명령입니다.
첫 번째 수는 행번호, 두 번째 수는 방향인데 0이면 왼쪽, 1이면 오른쪽이고, 세 번째 수는 회전하는 격자의 수입니다.
M개의 회전명령을 실행하고 난 후 아래와 같이 마당의 모래시계 모양의 영역에는 감 이 총 몇 개가 있는지 출력하는 프로그램을 작성하세요.
'''
import sys 
input = sys.stdin.readline
N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]
M = int(input())
 
for _ in range(M):
    rot = list(map(int, input().split()))
    col = rot[0]-1
    if rot[1] == 1: #오른쪽 이동
        m[col] = m[col][-rot[2]:] + m[col][:-rot[2]]
    elif rot[1] == 0: #왼쪽 이동
        m[col] = m[col][rot[2]:] + m[col][:rot[2]]
    
res =0
s,e = 0, N-1
for i in range(N):
    for j in range(s,e+1):
        res += m[i][j]      
    if i<N//2: # =을 넣어서 한참을 헤맸음
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1     
print(res)


