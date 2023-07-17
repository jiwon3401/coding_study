"""
숫자 카드는 정수 하나가 적혀져 있는 카드이다. 상근이는 숫자 카드 N개를 가지고 있다.
정수 M개가 주어졌을 때, 이 수가 적혀있는 숫자 카드를 상근이가 몇 개 가지고 있는지 구하는 프로그램을 작성하시오.
"""

import sys
input = sys.stdin.readline
N = int(input())
card = list(map(int, input().split()))
M = int(input())
card_list = list(map(int, input().split()))

card_dict={}
for i in card:
    if i in card_dict:
        card_dict[i] +=1
    else:
        card_dict[i] = 1

for i in range(M):
    if card_list[i] in card_dict:
        print(card_dict[card_list[i]], end=' ')
    else:
        print(0, end=' ')