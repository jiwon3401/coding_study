#[#Q7.교육과정 설계]

import sys 
from collections import deque 
input = sys.stdin.readline
a = input().rstrip().upper()
nums = int(input())
for n in range(nums):
    dq = deque(a)
    subject = input().rstrip().upper()
    for i in subject: 
        if i in dq:
            dq_pop = dq.popleft()
            if i != dq_pop: #필수과목 앞자료와 현재 과목과 일치하지 않으면 순서 어긋남.
                print(f"#{n+1} NO") 
                #print("#%d NO" %(n+1))
                break
    else: #순서가 통과해도 필수과목을 다 넣었는가.
        if len(dq) == 0: #전부 다 pop 
            print(f"#{n+1} YES")
        else:
            print(f"#{n+1} NO")
        