#1546

N = int(input())
score = list(map(int, input().split()))
M = max(score)

overall = 0
for i in range(len(score)):
    score[i] = score[i]/M*100
    overall += score[i]

print(overall/len(score))
