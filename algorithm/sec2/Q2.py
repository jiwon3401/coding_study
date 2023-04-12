#[2. K번째 수]

import sys
input = sys.stdin.readline
T = int(input())
for _ in range(T):  
    N,s,e,k = map(int, input().split())
    num = list(map(int, input().split()))
    num_list = num[s-1:e]
    print(sorted(num_list)[k-1]) 
   
    
##정답
import sys
sys.stdin=open('input.txt',"rt")
T = int(input())
for t in range(T):
    n,s,e,k = map(int, input().split())
    a = list(map(int, input().split()))
    a = a[s-1:e]
    a.sort()

    print("#%d %d" %(t+1, a[k-1])) ## 출력형식 !

'''
출력형식이 
#1 7
#2 6
이렇게 되어있으므로 맞춰줌.
'''