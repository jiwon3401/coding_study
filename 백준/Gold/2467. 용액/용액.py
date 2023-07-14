import sys
input=sys.stdin.readline
N= int(input())
ss = list(map(int, input().split()))
res = 2467000000
start = 0
end = N-1
s_min, s_max = 0,0

while start < end:
    if abs(ss[start]+ss[end]) < res:
        res = abs(ss[start]+ss[end])
        s_min, s_max = ss[start],ss[end]
    
    if ss[start]+ss[end]<0:
        start+=1 
    elif ss[start]+ss[end]:
        end-=1
    else:
        break
    
print(s_min, s_max)
