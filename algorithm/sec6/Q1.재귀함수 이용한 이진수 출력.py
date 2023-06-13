#[Q1. 재귀함수를 이용한 이진수 출력]
'''
10진수 N이 입력되면 2진수로 변환하여 출력하는 프로그램을 작성하세요. 단 재귀함수를 이용
해서 출력해야 합니다.
'''
import sys 
input = sys.stdin.readline


def binary(x):
    if x==0:
        return #함수 종료
    else:
        #print(x%2, end='')
        binary(x//2) 
        print(x%2, end='') #호출 밑으로 - stack 사용하므로 거꾸로 출력
    
if __name__== "__main__":
    N = int(input())
    binary(N)