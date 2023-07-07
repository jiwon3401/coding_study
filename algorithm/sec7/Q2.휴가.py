#[Q2.휴가(DFS)]
import sys
input = sys.stdin.readline

def DFS(time,total):
    global answer
    if time>N:
        return
    if time==N:
        if total>answer:
            answer= total  
    else:
        DFS(time+t[time], total+p[time])
        DFS(time+1, total)
    

if __name__=="__main__":
    N = int(input())
    answer=-1
    t,p = [],[]
    for _ in range(N):
        a,b = map(int, input().split())
        t.append(a)
        p.append(b)
    
    DFS(0,0)
    print(answer)