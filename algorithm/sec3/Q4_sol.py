import sys
input = sys.stdin.readline
n = int(input())
a = list(map(int, input().split()))
m = int(input())
b = list(map(int, input().split()))
p1=p2=0
c = [] 
#두 포인터 중 하나만 처리해도 끝나는것.

while p1 < n and p2 < m:
    if a[p1] <= b[p2]:
        c.append(a[p1])
        p1 += 1
    else:
        c.append(b[p2])
        p2 += 1
#하나의 자료가 먼저 멈추면 남은자료가 어딘지 확인
if p1<n:
    c = c+a[p1:]
if p2<m:
    c = c+b[p2:]

print(" ".join([str(i) for i in c]))
