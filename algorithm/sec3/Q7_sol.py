import sys
input = sys.stdin.readline 
n = int(input())
a = [list(map(int, input().split())) for _ in range(n)]
res = 0
s=e=n//2 # separate -> left/right

for i in range(n):
    for j in range(s,e+1): #가운데 원소들 더해주기
        res += a[i][j]
        
    if i<n//2:
        s -= 1
        e += 1
    else:
        s += 1
        e -= 1
print(res)