import sys
input = sys.stdin.readline 
N = int(input())
m = list(map(int, input().split()))
m.sort()
m_sum= 0
cnt = 0
for i in m:
    cnt += i
    m_sum += cnt 

print(m_sum)
