#[Q5.동전 분배하기(DFS)]

import sys
input = sys.stdin.readline

def DFS(L):
    global answer
    if L==N:
        if answer>(max(people)-min(people)):
            #3명의 금액이 다 달라야함 -> set 이용
            check=set()
            for i in people:
                check.add(i)
            if len(check)==3:
                answer = max(people)-min(people)   
    
    else:
        for i in range(len(people)):
            people[i]+= coin[L] #i번째 사람한테 coin을 주는 것
            DFS(L+1) 
            people[i]-= coin[L] #back 한것
    
    
if __name__=="__main__":
    N = int(input())
    people=[0]*3
    coin = []
    for _ in range(N):
        coin.append(int(input()))
    #total = sum(coin)
    answer = 1000000
    
    DFS(0)
    print(answer)