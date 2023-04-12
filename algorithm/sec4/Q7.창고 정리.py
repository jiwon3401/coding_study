#[#Q7. 창고정리]
'''
창고에 상자가 가로방향으로 일렬로 쌓여 있습니다. 
만약 가로의 길이가 7이라면 1열은 높이가 6으로 6개의 상자가 쌓여 있고, 2열은 3개의 상자, 3열은 9개의 상자가 쌓여 있으며 높이는 9라고 읽는다.
창고 높이 조정은 가장 높은 곳에 상자를 가장 낮은 곳으로 이동하는 것을 말한다.가장 높은 곳이나 가장 낮은 곳이 여러곳이면 그 중 아무거나 선택하면 된다.
창고의 가로 길이와 각 열의 상자 높이가 주어집니다. m회의 높이 조정을 한 후 가장 높은 곳과 가장 낮은 곳의 차이를 출력하는 프로그램을 작성하세요.
'''
import sys
input = sys.stdin.readline 
L = int(input())
height = list(map(int, input().split()))
M = int(input())

height.sort()

for i in range(M):
    height[L-1] -= 1
    height[0] += 1
    height.sort()

print(height[L-1]-height[0])