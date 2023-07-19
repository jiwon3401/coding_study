#[Q8.사과나무(BFS)]
import sys
input = sys.stdin.readline
from collections import deque 

N = int(input())
m = [list(map(int, input().split())) for _ in range(N)]

#상하좌우 탐색 [dx[i],dy[i]]
dx = [-1, 0, 1, 0]
dy = [0, 1, 0, -1]
check = [[0]*N for _ in range(N)] #방문 했는지 안했는지
check[N//2][N//2]=1 #중심부터 시작

#상하좌우 탐색 -> 마름모 모양
answer=0
answer+=m[N//2][N//2]
dq = deque()
dq.append((N//2,N//2)) #(tmp[0],tmp[1])
L=0

while True:
    if L==N//2:
        break
    size=len(dq) #level 별로 돌아가게됨
    for i in range(size):
        tmp=dq.popleft() #하나를 꺼내면 가지는 뻗어나감
        for j in range(4):
            x = tmp[0]+dx[j]
            y = tmp[1]+dy[j]
            if check[x][y]==0: #
                answer+=m[x][y]
                dq.append((x,y))
                check[x][y]=1
    #print(L, size)
    #for x in ch:
    #   print(x)
    L+=1 #level탐색 끝내면 +1 증가시킴

print(answer) 
      