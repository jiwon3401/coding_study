##[3. K번째 큰 수]
'''
1부터 100사이의 자연수가 적힌 N장의 카드를 가지고 있습니다. 같은 숫자의 카드가 여러장 있을 수 있습니다. 
이 중 3장을 뽑아 각 카드에 적힌 수를 합한 값을 기록하려고 합니다. 
3장을 뽑을 수 있는 모든 경우를 기록합니다. 기록한 값 중 K번째로 큰 수를 출력하는 프로그램을 작성하세요.
'''
import sys
from itertools import combinations
input = sys.stdin.readline
N, K = map(int, input().split())
card = list(map(int, input().split()))

card_comb = list(combinations(card,3))
sum = set()
for i in range(len(card_comb)):
    list_sum = 0
    for j in range(3):
        list_sum += card_comb[i][j]
        sum.add(list_sum)

print(list(sum)[len(sum)-K])


