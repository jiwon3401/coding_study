#가방문제(냅색 알고리즘)
'''
최고 17kg의 무게를 저장할 수 있는 가방이 있다. 그리고 각각 3kg, 4kg, 7kg, 8kg, 9kg의 무게를 가진 5종류의 보석이 있다. 
이 보석들의 가치는 각각 4, 5, 10, 11, 13이다. 이 보석을 가방에 담는데 17kg를 넘지 않으면서 최대의 가치가 되도록 하려면 
어떻게 담아야 할까요? 각 종류별 보석의 개수는 무한이 많다. 한 종류의 보석을 여러 번 가방에 담을 수 있다는 뜻입니다.
'''
import sys 
input=sys.stdin.readline

#if__name__=="__main__":
n,l = list(map(int, input().split()))
dy=[0]*(l+1) #dy[j]: 가방에 j무게를 담을 때의 보석의 최대 가치
for i in range(n):
    w, v = list(map(int, input().split())) #w:무게, v:가치 -> 매 보석마다 갱신
    for j in range(w,l+1):
        dy[j]=max(dy[j-w]+v, dy[j]) #dy[j-w]+v: v가치의 무게를 담는다고 가정했으므로 w의 공간을 남겨둠
    #print(dy) 어떻게 변하는지 확인해보기
        
print(dy[l])
