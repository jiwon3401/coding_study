import sys 
input = sys.stdin.readline
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
m = int(input())
for i in range(m):
    h, t, k = map(int, input().split())
    if t == 0: #왼쪽으로 회전
        for _ in range(k):
            a[h-1].append(a[h-1].pop(0)) #맨 앞을 빼서 append
    else: #오른쪽으로 회전
        for _ in range(k):
            a[h-1].insert(0, a[h-1].pop()) #마지막을 빼서 앞에 insert

res = 0
s=0
e=n-1
for i in range(n):
    for j in range(s,e+1):
        res+=a[i][j]
    if i < n//2:
        s += 1
        e -= 1
    else:
        s -= 1
        e += 1
print(res)
