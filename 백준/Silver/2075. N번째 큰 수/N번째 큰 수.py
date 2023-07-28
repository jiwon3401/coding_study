import sys 
input = sys.stdin.readline
n = int(input())
bb = []
for _ in range(n):
    bb+=list(map(int,input().split())) #append하면 2차원리스트로 들어가게 되므로 += 사용
    bb = sorted(bb, reverse=True)[:n]
    
print(bb[-1])