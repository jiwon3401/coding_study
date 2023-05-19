#네트워크 선 자르기(Top-Down : 재귀, 메모이제이션)

import sys

def DFS(v):
    if v==1 or v==2: #dy[1]=1, dy[2]=2
        return v
    else:
        dy[v]=DFS(v-1)+DFS(v-2)
        return dy[v]


if __name__=="__main__":
    N = int(input())
    dy = [0]*(N+1)

    print(DFS(N))