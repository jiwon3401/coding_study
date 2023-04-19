#[#Q9. 침몰하는 타이타닉]
'''
유럽에서 가장 유명했던 유람선 타이타닉이 침몰하고 있습니다. 유람선에는 N명의 승객이 타고 있습니다. 
구명보트를 타고 탈출해야 하는데 타이타닉에 있는 구명보트는 2명 이하로만 탈 수 있으며, 보트 한 개에 탈 수 있는 총 무게도 M kg 이하로 제한되어 있습니다.
N명의 승객 몸무게가 주어졌을 때 승객 모두가 탈출하기 위한 구명보트의 최소개수를 출력하는 프로그램을 작성하세요.
'''
import sys
input = sys.stdin.readline 
N,M = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
cnt = 0
# 가장 무거운 사람+가벼운 사람 먼저 고려한 뒤, pop 시키면서 나가기

while w: #자료구조 비기 전까지
    if len(w) ==1: #한명이 남았을때 고려를 해줘야함!
        cnt+=1
        break 
    
    if w[0] + w[-1] > M:
        w.pop()
        cnt += 1
        
    else:
        w.pop(0) 
        w.pop()
        cnt += 1
print(cnt)

# 리스트는 pop 시키면 한칸씩 앞으로 당겨옴 -> 비효율적
# deque는 앞,뒤에서 빼도 자료가 움직이지 않음 
from collections import deque
N,M = map(int, input().split())
w = list(map(int, input().split()))
w.sort()
w = deque(w) 
cnt = 0 

while w:
    if len(w)==1:
        cnt += 1
        break
    if w[0]+w[-1]>M:
        w.pop()
        cnt+=1
    else:
        w.popleft() #deque는 popleft() 사용
        w.pop()
        cnt += 1
print(cnt)