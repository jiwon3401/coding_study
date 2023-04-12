#[#Q7. 사과나무(다이아몬드)]
'''
현수의 농장은 N*N 격자판으로 이루어져 있으며, 각 격자안에는 한 그루의 사과나무가 심어저있다. N의 크기는 항상 홀수이다. 
가을이 되어 사과를 수확해야 하는데 현수는 격자판안의 사과를 수확할 때 다이아몬드 모양의 격자판만 수확하고 나머지 격자안의 사과는 새들을 위해서 남겨놓는다.
현수과 수확하는 사과의 총 개수를 출력하세요.
'''
import sys
input = sys.stdin.readline 
N = int(input())
tree = [list(map(int, input().split())) for _ in range(N)]

apple = 0
for i in tree[N//2]:
    apple += i

for i in range(N//2):
    for j in tree[i][(N//2-i):(N//2+i+1)]:
        apple += j
    for j in tree[N-1-i][(N//2-i):(N//2+i+1)]:
        apple += j
print(apple)
