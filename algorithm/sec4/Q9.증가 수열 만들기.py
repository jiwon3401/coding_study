#[#Q9. 증가수열 만들기(그리디)]
'''
1부터 N까지의 모든 자연수로 구성된 길이 N의 수열이 주어집니다. 이 수열의 왼쪽 맨 끝 숫자 또는 오른쪽 맨 끝 숫자 중 하나를 가져와 나열하여 
가장 긴 증가수열을 만듭니다. 이때 수열에서 가져온 숫자(왼쪽 맨 끝 또는 오른쪽 맨 끝)는 그 수열에서 제거됩니다.

첫째 줄에 최대 증가수열의 길이를 출력합니다.
두 번째 줄에 가져간 순서대로 왼쪽 끝에서 가져갔으면 ‘L', 오른쪽 끝에서 가져갔으면 ’R'를 써간 문자열을 출력합니다.
(단 마지막에 남은 값은 왼쪽 끝으로 생각합니다.)
'''
import sys
input = sys.stdin.readline 
N = int(input())
a = list(map(int, input().split()))

tmp=0 #마지막에 저장되는 변수를 만들어주기
alpha=[] #굳이 리스트 만들지 않고 ""로 받는게 더 좋음

while a:
    if a[0]<tmp and a[-1]<tmp:
        break
    elif a[0]>tmp and a[-1]>tmp:
        if len(a)==1:
            alpha.append('L')
            break
        elif a[0]<a[-1]:
            tmp = a[0]
            a.pop(0)
            alpha.append('L')
        elif a[0]>a[-1]:
            tmp = a[-1]
            a.pop()
            alpha.append('R')
    elif a[0]>tmp and a[-1]<tmp:
        tmp=a[0]
        a.pop(0)
        alpha.append('L')
    elif a[0]<tmp and a[-1]>tmp:
        tmp=a[-1]
        a.pop()
        alpha.append('R')

print(len(''.join(alpha)),''.join(alpha),sep='\n')
