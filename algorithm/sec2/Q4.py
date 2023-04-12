#[#4. 대표값]
'''
N명의 학생의 수학점수가 주어집니다. N명의 학생들의 평균(소수 첫째자리 반올림)을 구하고,
N명의 학생 중 평균에 가장 가까운 학생은 몇 번째 학생인지 출력하는 프로그램을 작성하세요.
평균과 가장 가까운 점수가 여러 개일 경우 먼저 점수가 높은 학생의 번호를 답으로 하고, 
높은 점수를 가진 학생이 여러 명일 경우 그 중 학생번호가 빠른 학생의 번호를 답으로 합니다.
'''

import sys
input = sys.stdin.readline
N = int(input())
score = list(map(int, input().split()))
#avg = round(sum(score)/N,0) #round는 가까운 짝수값으로 올려주므로 round 사용하면 안됨 !
avg = int(sum(score)/N + 0.5)

avgMin = float('inf')
for idx, i in enumerate(score):
    avg_diff = abs(avg-i)
    if avg_diff < avgMin:
        avgMin = avg_diff
        avg_student, avg_index = i, idx+1

    elif avg_diff == avgMin: #뒤에 나오는 요소들과 비교해야함
        if i > avg_student: 
            avg_student, avg_index = i, idx+1
print(avg_student, avg_index)
        
            

