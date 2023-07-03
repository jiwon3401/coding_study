import sys
n,m = map(int, input().split())
#n:노드번호, m:간선개수
g = [[0]*(n+1) for _ in range(n+1)] #그래프 정보: 0으로 초기화

for i in range(m):
    a,b,c = map(int, input().split())
    # #무방향그래프
    # g[a][b]=1
    # g[b][a]=1
    g[a][b]=c

for i in range(1,n+1):
    for j in range(1,n+1):
        print(g[i][j], end=' ')
    print()