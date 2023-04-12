#[#Q6.씨름선수(그리디)]
'''
현수는 씨름 감독입니다. 현수는 씨름 선수를 선발공고를 냈고, N명의 지원자가 지원을 했습니다. 
현수는 각 지원자의 키와 몸무게 정보를 알고 있습니다. 현수는 씨름 선수 선발 원칙을 다음과 같이 정했습니다.
“다른 모든 지원자와 일대일 비교하여 키와 몸무게 중 적어도 하나는 크거나, 무거운 지원자만 뽑기로 했습니다.”
만약 A라는 지원자보다 키도 크고 몸무게도 무거운 지원자가 존재한다면 A지원자는 탈락입니다.
'''
import sys
input = sys.stdin.readline 
N = int(input())
a = []
for _ in range(N):
    h, w = list(map(int,input().split()))
    a.append([h,w])

a.sort(key = lambda x: -x[0]) #키 정렬
#tall = a[0][0]
cnt = 0 
heavy = 0
for i in range(N):
    if a[i][1] > heavy:
        largest = a[i][1]
        cnt+=1
        #print(a[i])
print(cnt)