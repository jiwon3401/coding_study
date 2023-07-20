#[Q9.미로의 최단거리 통로(BFS)]
import sys
input = sys.stdin.readline
from collections import deque 

m = [list(map(int, input().split())) for _ in range(7)]
## mm=m.copy()
check = [[0]*7 for _ in range(7)] #몇번만에 갈수있는지 체크
m[0][0]=1 #방문했으니 벽으로 만들기
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]

dq = deque()
dq.append((0,0))

while dq:
    pos = dq.popleft()
    
    for i in range(4): #상하좌우
        x=pos[0]+dx[i]
        y=pos[1]+dy[i]
        
        if 0<=x<=6 and 0<=y<=6 and m[x][y]!=1: #도로인 경우
            m[x][y]=1 #벽으로 만들어서 다신 못가게 하기
            check[x][y]=check[pos[0]][pos[1]]+1
            dq.append((x,y))

if check[6][6]==0:
    print(-1)
else:
    print(check[6][6])
