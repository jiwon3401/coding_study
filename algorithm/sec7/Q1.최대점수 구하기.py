#[Q1.최대점수 구하기(DFS)]
import sys
input = sys.stdin.readline

def DFS(p,score,time):
    #p:문제번호, score:점수, time:걸리는 시간
    global tmp
    if time>M: #시간제한
        return 
    if p==N: #부분집합 완성
        if score>answer: #얻는점수
            answer=score
        else:
            DFS(p+1, score+s[p], time+t[p]) #다음문제, 얻는점수, 사용한 시간
            DFS(p+1, score, time) #문제 안풀고 넘어갈 경우
         

if __name__=="__main__":
    N,M = map(int, input().split())
    s, t = [],[]
    for _ in range(N):
        a,b = map(int, input().split())
        s.append(a)
        t.append(b)    
    answer=-1000000
    DFS(0,0,0)
    print(answer)