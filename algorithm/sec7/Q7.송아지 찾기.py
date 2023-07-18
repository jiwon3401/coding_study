#[Q7.송아지 찾기(BFS)]
#BFS 넓이우선탐색
import sys
input = sys.stdin.readline
from collections import deque

s, e = map(int, input().split())
jump = [0]*10001 #직선 좌표 1~10000 
chk =  [0]*10001 #방문했는지 체크

jump[s]=0 #level0 의미
chk[s]=1 #방문했으므로 체크해주기

dq = deque()
dq.append(s)

while dq:
    tmp = dq.popleft() #s부터 pop (level 0부터 차례대로)
    if tmp==e:
        break
    for i in (tmp-1, tmp+1, tmp+5): #가지 3개로 뻗어나가기
        if 0<tmp<=10000:
            if chk[i]==0: #방문하지 않은 곳만
                dq.append(i)
                chk[i]=1
                jump[i]=jump[tmp]+1 #가지 계속 뻗기 0,1,...
                
print(jump[e])             
                