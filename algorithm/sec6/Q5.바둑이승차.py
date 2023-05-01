#바둑이 승차(DFS)
'''
철수는 그의 바둑이들을 데리고 시장에 가려고 한다. 그런데 그의 트럭은 C킬로그램 넘게 태울수가 없다. 
철수는 C를 넘지 않으면서 그의 바둑이들을 가장 무겁게 태우고 싶다.
N마리의 바둑이와 각 바둑이의 무게 W가 주어지면, 철수가 트럭에 태울 수 있는 가장 무거운 무게를 구하는 프로그램을 작성하세요.
'''
import sys 
input = sys.stdin.readline

def DFS(v):
    global w_max
    if v==N:
        w_sum=0
        for i in range(N):
            if ck[i]==1:
                w_sum+=weight[i]
        if w_sum>C: #종료조건: C이상
            return
        if w_sum>w_max: 
            w_max=w_sum #global 선언해줘야함.
    else:
        ck[v]=1 #바둑이 탑승하실게여 ~
        DFS(v+1)
        #####
        ck[v]=0
        DFS(v+1)
    
if __name__=="__main__":
    C, N = map(int, input().split())
    weight = []
    for _ in range(N):
        weight.append(int(input()))
    w_max = 0
    ck = [0]*N
    DFS(0)
    print(w_max)