import sys
input = sys.stdin.readline 
K = int(input())
money = []
for _ in range(K):
    mm = int(input())
    if mm == 0:
        money.pop()
    else:
        money.append(mm)

print(sum(money))