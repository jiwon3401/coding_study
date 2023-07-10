#[Q2.양팔저울(DFS)]
import sys
input = sys.stdin.readline

def DFS(v,water): 
    #v: 추 무게를 접근하는 index, sum: 측정할 수 있는 물의 무게(왼쪽:+1, 오른쪽:-1)
    global res
    if v==K:
        if 0<water<=sum(weight):
            res.add(water)

    else:
        DFS(v+1, water+weight[v]) #물 왼쪽
        DFS(v+1, water-weight[v]) #물 오른쪽
        DFS(v+1, water) #그대로


if __name__=="__main__":
    K = int(input())
    weight = list(map(int, input().split()))
    res = set() #측정될수있는무게 -> 중복되는 무게를 처리하기 위해 set 사용
    DFS(0,0)
    print(sum(weight) - len(res))

        