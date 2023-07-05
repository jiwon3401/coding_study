import sys
import itertools
from itertools import permutations

input = sys.stdin.readline
N,F = map(int, input().split())
binary = [1]*N
cnt = 0
for i in range(1,N):
    binary[i]=binary[i-1]*(N-i)//i
    
    
for tmp in permutations(list(range(1,N+1))):  
    sum=0
    for l,x in enumerate(tmp):
        sum+=(x * binary[l])
        
    if sum == F:
        for x in tmp:
            print(x, end=' ')
        break