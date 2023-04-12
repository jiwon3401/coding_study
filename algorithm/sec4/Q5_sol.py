import sys
input = sys.stdin.readline 
n = int(input())
meeting = []
for i in range(n):
    s, e = map(int, input().split())
    meeting.append((s,e)) #tuple
meeting.sort(key=lambda x: (x[1],x[0])) #end-> start 정렬순위 지정

et = 0 #회의끝나는시간
cnt = 0 
for s, e in meeting:
    if s >= et:
        et = e
        cnt += 1
print(cnt)
