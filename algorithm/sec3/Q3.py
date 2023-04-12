#[#Q3. 카드 역배치]
'''
1부터 20까지 숫자가 하나씩 쓰인 20장의 카드가 아래 그림과 같이 오름차순으로 한 줄로 놓여있다. 
각 카드의 위치는 카드 위에 적힌 숫자와 같이 1부터 20까지로 나타낸다.
이제 다음과 같은 규칙으로 카드의 위치를 바꾼다: 구간 [a, b] (단, 1 ≤ a ≤ b ≤20)가 주어지면 
위치 a부터 위치 b까지의 카드를 현재의 역순으로 놓는다. 이 상태에서 구간 [9, 13]이 다시 주어진다면, 
위치 9부터 위치 13까지의 카드 6, 5, 11, 12, 13을 역순으로 하여 13, 12, 11, 5, 6으로 놓는다. 
오름차순으로 한 줄로 놓여있는 20장의 카드에 대해 10개의 구간이 주어지면, 주어진 구간의 순서대로 
위의 규칙에 따라 순서를 뒤집는 작업을 연속해서 처리한 뒤 마지막 카드들의 배치를 구하는 프로그램을 작성하시오.
'''

import sys
input = sys.stdin.readline
card = list(range(1,21))

for _ in range(10):
    a, b = map(int, input().split())
    card[a-1:b] = card[a-1:b][::-1]
    
print(" ".join([str(i) for i in card]))  
    
    
#sol
import sys
sys.stdin = open("input.txt","rt")
a = list(range(21))

for _ in range(10):
    s, e = map(int,input().split())
    for i in range((e-s+1)//2): #s~e범위 -> 반만 돌기
        a[s+i], a[e-i] = a[e-i], a[s+i]
a.pop(0) #제일 앞에꺼 없애기 #그냥 처음부터 범위에 맞게 리스트 만들면 안되나

for x in a:
    print(x, end=' ')