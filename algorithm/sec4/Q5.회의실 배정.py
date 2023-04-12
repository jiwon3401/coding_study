#[#Q5.회의실배정(그리디)]
'''
한 개의 회의실이 있는데 이를 사용하고자 하는 n개의 회의들에 대하여 회의실 사용표를 만들려고 한다. 
각 회의에 대해 시작시간과 끝나는 시간이 주어져 있고, 각 회의가 겹치지 않게 하면서 회의실을 사용할 수 있는 최대수의 회의를 찾아라. 
단, 회의는 한번 시작하면 중간에 중단될 수 없으며 한 회의가 끝나는 것과 동시에 다음 회의가 시작될 수 있다.
'''
import sys
input = sys.stdin.readline 
n = int(input())
pq = []
for _ in range(n):
    p,q = list(map(int, input().split()))
    pq.append([p,q])
pq.sort(key=lambda x:x[0])
pq.sort(key=lambda x:x[1]) 
#pq.sort(key=labmda x: (x[1],x[0])) #한번에 가능함.

cnt = 1
end = pq[0][1]
for i in range(1,n):
    if pq[i][0]>=end: #시작>=끝
        cnt += 1
        end = pq[i][1]
print(cnt)