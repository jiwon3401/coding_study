#[#Q1.가장 큰 수]
'''
선생님은 현수에게 숫자 하나를 주고, 해당 숫자의 자릿수들 중 m개의 숫자를 제거하여 가장 큰 수를 만들라고 했습니다. 
여러분이 현수를 도와주세요.(단 숫자의 순서는 유지해야 합니다)
'''
import sys
input = sys.stdin.readline
aa, n = map(int, input().split())
aa = list(map(int, str(aa)))

stack =[]
#스택 - last in first out/ list를 이용해서 stack을 하는 것.

for a in aa:
    while stack and n>0 and a>stack[-1]: #stack이 비어있지않고,나중에 들어오는게 현재보다 더 작을때
        stack.pop()
        n-=1 #pop 시켜야할 개수
    stack.append(a)
    
#n개를 전부 다 지우지 못한 경우 
if n!=0:
    stack=stack[:n]  #내림차순으로 이미 stack되어있으므로 인덱싱 슬라이싱 사용해서 제거

print("".join(map(str, stack)))

