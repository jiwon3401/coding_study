import sys
input = sys.stdin.readline
sys.setrecursionlimit(10**6)


def dfs(v):
    global cnt
    check[v]=cnt #방문한 노드 체크하기
    for i in sorted(graph[v]):
        if not check[i]:
            cnt+=1
            dfs(i)
    
if __name__=="__main__":
    N,M,R = map(int, input().split())
    graph = [[] for _ in range(N+1)]
    check = [0]*(N+1) #노드정보 저장
    cnt=1
    for _ in range(M):
        u,v = map(int, input().split())
        graph[u].append(v) ###
        graph[v].append(u)
    
    dfs(R) #시작정점 = 1 = R
    
    for i in range(1,N+1):
        print(check[i])