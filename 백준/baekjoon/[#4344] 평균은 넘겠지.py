'''
각 케이스마다 한 줄씩 평균을 넘는 학생들의 비율을 반올림하여 소수점 셋째 자리까지 출력한다.
'''

C = int(input())
for _ in range(C):
    score = list(map(int, input().split()))
    count = 0
    for s in range(1, len(score)):
        if score[s] > sum(score[1:])/score[0]:
            count += 1
    rate = count/score[0]*100
    print("{:.3f}".format(rate)+"%")
    #print("{:.3f}".format(round(rate*100,3))+"%")
