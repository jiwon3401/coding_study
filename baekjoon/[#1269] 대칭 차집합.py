
'''
자연수를 원소로 갖는 공집합이 아닌 두 집합 A와 B가 있다. 이때, 두 집합의 대칭 차집합의 원소의 개수를 출력하는 프로그램을 작성하시오. 
두 집합 A와 B가 있을 때, (A-B)와 (B-A)의 합집합을 A와 B의 대칭 차집합이라고 한다.
'''
import sys
input = sys.stdin.readline
x, y = map(int, input().split())
a = list(map(int, input().split()))
b = list(map(int, input().split()))
print(len(set(a)-set(b))+ len(set(b)-set(a)))