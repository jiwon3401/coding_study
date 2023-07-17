#[Q6.알파코드(DFS)]

import sys
input = sys.stdin.readline()
import string

def DFS(L,p):
    global answer
    if L==N:
        answer+=1
        for i in range(p):
            if res[i]==0:
                pass
            else:
                print(alphabet[res[i]], end='')
        print()
        
        
    for i in range(1,27): #알파벳 전체 순회
        if i<10:
            if num[L]==i:
                res[p]=i
                DFS(L+1, p+1)  
        
        else:               
            if num[L]==i//10 and num[L+1]==i%10:
                res[p]=i
                DFS(L+2, p+1)    


if __name__=="__main__":
    num = list(map(int, sys.stdin.readline().strip()))
    N = len(num)
    num.insert(N,-1)
    res = [0]*(N+1)
    alphabet = dict(zip(range(1,27), list(string.ascii_uppercase)))
    answer = 0
    DFS(0,0)
    print(answer)
    